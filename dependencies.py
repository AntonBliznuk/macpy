import subprocess


def is_brew_installed() -> None:
    try:
        subprocess.run(
            ["brew", "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Brew is installed.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"❌ Brew is not instelled.\nInstall it here: https://brew.sh/")


def is_dependencies_installed(dependencies: list[dict]) -> None:
    for d in dependencies:
        t = d.get("type")
        n = d.get("name")
        try:
            subprocess.run(
                ["brew", "list", f"--{t}", n],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"✅ {n} is installed.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"❌ {n} is not installed.\nInstall it with this command: brew install --{t} {n}")


def is_shortcuts_available(shortcuts: list[dict]) -> None:
    result = subprocess.run(
        ["shortcuts", "list"],
        capture_output=True,
        text=True,
        check=True
    )
    existing = result.stdout.splitlines()

    for s in shortcuts:
        name = s.get("name")
        desc = s.get("description")

        if name in existing:
            print(f"✅ {name} is available.")
        else:
            raise Exception(
                f"❌ {name} is not available.\n"
                f"Create it in the Shortcuts app with this name: {name}\n"
                f"Description: {desc}"
            )


def default_dependencies_check() -> None:
    print("Brew: ")
    is_brew_installed()

    print("Dependencies: ")
    is_dependencies_installed(
        [
            {
                "type": "formula",
                "name": "displayplacer"
            },
            {
                "type": "formula",
                "name": "blueutil"
            },
            {
                "type": "cask",
                "name": "cloudflare-warp"
            },
        ]
    )

    print("Shortcuts: ")
    is_shortcuts_available(
        [
            {
                "name": "Motion-on",
                "description": "Turns off motion"
            },
            {
                "name": "Motion-off",
                "description": "Turns off motion"
            },
            {
                "name": "Transparency-off",
                "description": "Turns off motion"
            },
            {
                "name": "Transparency-on",
                "description": "Turns off motion"
            },
        ]
    )

    print("Status: \n✅ Ready to operate ✅")


if __name__ == "__main__":
    default_dependencies_check()

