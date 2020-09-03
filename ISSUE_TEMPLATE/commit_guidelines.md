# Commit message guidelines

A good commit message should describe what changed and why.

1. The first line should:
 - contain a short description of the change (preferably around 50 characters or less)
 - be entirely in lowercase with the exception of proper nouns, acronyms, and the words that refer to code, like function/variable names
 - be prefixed with the name of the changed subsystem and start with an imperative verb. Check the output of git log --oneline files/you/changed to find out what subsystems your changes touch. e.g. `- src: fix typos in file.name`

2. Keep the second line blank. If your patch fixes an open issue, you can add a reference to it at the end of the log. Use the Fixes: prefix and the full issue URL. For other references use Refs: e.g `Fixes: https://github.com/[repo]/issues/1337`, `Refs: https://eslint.org/docs/rules/space-in-parens.html` ans `Refs: https://github.com/[repo]/pull/3615`

3. If your commit introduces a breaking change (semver-major), it should contain an explanation about the reason of the breaking change, which situation would trigger the breaking change and what is the exact change.
