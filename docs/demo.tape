# Same demo as demo.gif, for charmbracelet/vhs:  vhs docs/demo.tape
# (docs/render_demo.py draws the committed GIF without needing vhs.)
Output docs/demo.gif
Set Shell "bash"
Set FontSize 16
Set Width 960
Set Height 560
Set Padding 20
Set TypingSpeed 35ms
Set Theme "Dracula"
Hide
Type "PS1='you> ' && clear"
Enter
Show
Type "echo 'hey can you deploy the pine cone shop checkout fix no wait dont push yet just commit it and uh bump the version to one point four oh'"
Enter
Sleep 1s
Hide
Type "printf '\nWithout the rule\n  Did you mean Pinecone Shop? Do you want me to push or not? What is one point four oh?\n'"
Enter
Show
Sleep 3s
Hide
Type "printf '\nWith the rule\n  Understood as: commit the checkout fix in pinecone-shop, do not push, version 1.4.0.\n  Committed. Version bumped to 1.4.0. Not pushed.\n'"
Enter
Show
Sleep 3s
