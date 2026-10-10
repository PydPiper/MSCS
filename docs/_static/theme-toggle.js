(() => {
    const themeLink = document.querySelector('link[href*="/dist/theme/"]');
    const presentation = document.querySelector(".reveal");

    if (!themeLink || !presentation) {
        throw new Error("Could not find the Reveal.js theme or presentation.");
    }

    const themeDirectory = new URL(".", themeLink.href);
    const button = document.createElement("button");
    button.className = "theme-toggle";
    button.type = "button";
    button.setAttribute("aria-pressed", "false");

    let lightMode = new URL(themeLink.href).pathname.endsWith("/white.css");

    const updateTheme = () => {
        const nextTheme = lightMode ? "white.css" : "black.css";
        themeLink.href = new URL(nextTheme, themeDirectory).href;
        button.textContent = lightMode ? "Dark mode" : "Light mode";
        button.setAttribute("aria-label", `Switch to ${lightMode ? "dark" : "light"} mode`);
        button.setAttribute("aria-pressed", String(lightMode));
    };

    button.addEventListener("click", () => {
        lightMode = !lightMode;
        updateTheme();
    });

    updateTheme();
    presentation.append(button);
})();
