# Terminal Profile

## Questions

- How to switch between shell?
- How to set default shell on mac?
- How to set prompt and color on shell?
- Use which file to set command?
- How to change shell setting in Visual Studio Code?

## Codes

```bash
# switching shell
bash
zsh
```

```bash
# .bash_profile
function prompt
{
    local BrightGreen='\e[0;92m'
    local BrightMagenta='\e[0;95m'
    local BrightCyan='\e[0;96m'
    export PS1="
${BrightGreen}[\t][\u@\h]: ${BrightMagenta}\w
${BrightCyan}$ "
}
prompt
```

```bash
# .zshrc
function prompt
{
    local Green1='%46F'
    local Magenta1='%201F'
    local Cyan1='%51F'
    export PS1="
${Green1}[%*][%n@%m]: ${Magenta1}%~ 
${Cyan1}\$ "
}
prompt
```

## References
- [bash prompt](https://www.gnu.org/software/bash/manual/bash.html#Controlling-the-Prompt)
- [bash color](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
- [zsh prompt](https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html#Prompt-Expansion)
- [zsh color](https://www.ditig.com/256-colors-cheat-sheet)
- [zsh files](https://zsh.sourceforge.io/Doc/Release/Files.html#Startup_002fShutdown-Files)
- [Visual Studio Code - Integrated Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal)