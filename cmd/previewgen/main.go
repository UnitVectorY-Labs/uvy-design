// previewgen renders application-based design specimens without changing consumers.
package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"math"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

type Page struct {
	Title, Kind, Project, Repository string
	Data                             map[string]any
	Selected                         map[string]any
}

func fixture(name string) map[string]any {
	b, e := os.ReadFile("prototypes/fixtures/" + name + ".json")
	must(e)
	var v map[string]any
	must(json.Unmarshal(b, &v))
	return v
}
func icon(name string) template.HTML {
	b, e := os.ReadFile("prototypes/icons/" + name + ".svg")
	must(e)
	s := string(b)
	s = strings.Replace(s, "<svg", `<svg class="icon" aria-hidden="true" focusable="false"`, 1)
	return template.HTML(s) // Only pinned, reviewed repository SVG files are accepted.
}
func luminance(hex string) float64 {
	n, e := strconv.ParseUint(strings.TrimPrefix(hex, "#"), 16, 32)
	must(e)
	a := func(c uint64) float64 {
		v := float64(c) / 255
		if v <= .04045 {
			return v / 12.92
		}
		return math.Pow((v+.055)/1.055, 2.4)
	}
	return .2126*a(n>>16) + .7152*a((n>>8)&255) + .0722*a(n&255)
}
func ink(hex string) string { // Preserve the original data hue; fix text by luminance.
	l := luminance(hex)
	if (l+.05)/.05 >= 1.05/(l+.05) {
		return "#000000"
	}
	return "#ffffff"
}
func metricStyle(hex string) template.CSS {
	if len(hex) != 7 || !strings.HasPrefix(hex, "#") {
		panic("invalid metric color")
	}
	_, e := strconv.ParseUint(hex[1:], 16, 32)
	must(e)
	return template.CSS(fmt.Sprintf("background-color:%s;color:%s", hex, ink(hex)))
}
func main() {
	must(os.MkdirAll("output/snippets", 0755))
	must(os.MkdirAll("output/vendor", 0755))
	data := map[string]any{"Unreleased": fixture("unreleased"), "Repo": fixture("repo-detail"), "JWKS": fixture("jwks"), "Cert": fixture("certificate")}
	funcs := template.FuncMap{"icon": icon, "metricStyle": metricStyle,
		"endpointRows": func(values map[string]any) []map[string]string {
			var rows []map[string]string
			for _, label := range []string{"OpenID Configuration", "OAuth 2.0 Authorization Server Metadata", "JWKS URI"} {
				if value, ok := values[label].(string); ok {
					rows = append(rows, map[string]string{"label": label, "url": value})
				}
			}
			return rows
		}, "short": func(s string) string {
			if len(s) > 7 {
				return s[:7]
			}
			return s
		}}
	t := template.Must(template.New("page.html").Funcs(funcs).ParseFiles("prototypes/page.html", "prototypes/jwks-content.html"))
	pages := map[string]Page{
		"index.html":              {"Design review", "review", "Design review", "uvy-design", data, nil},
		"table.html":              {"Unreleased Commits", "table", "Unreleased Commits", "unreleasedcommits", data, nil},
		"repository.html":         {"adk-docker-base · Unreleased Commits", "repository", "Unreleased Commits", "unreleasedcommits", data, nil},
		"workbench.html":          {"certsummary", "workbench", "certsummary", "certsummary", data, nil},
		"catalog.html":            {"JWKS Catalog", "catalog", "JWKS Catalog", "jwks-catalog", data, data["JWKS"].(map[string]any)["selected"].(map[string]any)},
		"service-1worldsync.html": {"1WorldSync · JWKS Catalog", "catalog", "JWKS Catalog", "jwks-catalog", data, data["JWKS"].(map[string]any)["selected"].(map[string]any)},
	}
	other := fixture("jwks-3d-systems")
	pages["service-3d-systems.html"] = Page{"3D Systems · JWKS Catalog", "catalog", "JWKS Catalog", "jwks-catalog", data, other["selected"].(map[string]any)}
	for name, p := range pages {
		f, e := os.Create(filepath.Join("output", name))
		must(e)
		must(t.ExecuteTemplate(f, "page.html", p))
		must(f.Close())
		if strings.HasPrefix(name, "service-") {
			f, e = os.Create(filepath.Join("output/snippets", name))
			must(e)
			must(t.ExecuteTemplate(f, "jwks-fragment", p))
			must(f.Close())
		}
	}
	// Keep the previous local review URL as a full page alias, not a new navigation tab.
	b, e := os.ReadFile("output/service-1worldsync.html")
	must(e)
	must(os.WriteFile("output/detail.html", b, 0644))
	for _, name := range []string{"style.css", "theme.js", "demo.js", "vendor/htmx-4.0.0.min.js"} {
		b, e := os.ReadFile(filepath.Join("prototypes", name))
		must(e)
		must(os.WriteFile(filepath.Join("output", name), b, 0644))
	}
	for source, target := range map[string]string{
		"THIRD_PARTY_NOTICES.txt":        "THIRD_PARTY_NOTICES.txt",
		"prototypes/icons/LICENSE":       "vendor/TABLER-ICONS-LICENSE",
		"prototypes/vendor/HTMX-LICENSE": "vendor/HTMX-LICENSE",
	} {
		b, e := os.ReadFile(source)
		must(e)
		must(os.WriteFile(filepath.Join("output", target), b, 0644))
	}

}
func must(e error) {
	if e != nil {
		panic(e)
	}
}
