from conan import ConanFile, tools
from conan.tools.meson import MesonToolchain, Meson
from conan.tools.gnu import PkgConfigDeps

class KLangApplication(ConanFile):
    name = "k-lang"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = (
        "MesonToolchain",
        "PkgConfigDeps"
    )
    requires = (
        "gtk/system",
        "sqlite3/3.44.0"
    )
    exports_sources = "src/*"

    def layout(self):
        self.folders.build = "build"

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()
