# Voice input

The person you work with dictates most requests through speech-to-text (Wispr Flow, macOS dictation, Whisper, phone voice typing). Treat recognition errors as typos, not as intent.

## What goes wrong in dictation

- Proper nouns: project names, brands, domains, file names, commands.
- English terms written phonetically in another script, or words split and glued wrongly ("get hub", "post gres").
- Numbers, amounts, IDs, email addresses, keys. These break most often.
- Punctuation: commas and periods in random places. Two requests may fuse into one sentence; one may split into two.
- Fragments: the start of a sentence is missing, or a stray word trails at the end.
- Negation: "don't" or "not" dropped or inserted. The most dangerous category.

## How to work

1. **Recover the meaning yourself first.** Use the active project, recent messages, the project list, and the glossary. A name that sounds like a known project almost always is that project.
2. **Don't ask because the form is messy.** Grammar, word order, and odd endings are ignored silently.
3. **Don't quote the mistake and don't correct the user.** If the recovery is not obvious, start your reply with one line: `Understood as: ...`, then do the work.
4. **Two equally likely readings: ask.** One short question with the options, not a list of clarifications.
5. **Irreversible step on a heard value: verify against the source.** Domain, amount, email, ID, table name: check the config, dashboard, or database before deploying, sending, paying, or deleting.

## Always ask when

- The target is ambiguous: two similar-sounding projects, accounts, domains, or mailboxes.
- You can't tell whether a negation is there ("push" vs "don't push").
- It involves **money, production, deletion, or sending something outside** (email, messages, posts, submissions). The bar for asking is lower here. "Almost sure" doesn't cancel the cost of being wrong.

For everything else, a needless question caused by bad audio is friction, not caution. Act.

## Example

Heard: `hey deploy the pine cone checkout fix no wait dont push yet just commit it and bump to one point four oh`

Reply starts: `Understood as: commit the checkout fix in pinecone-shop, do not push, version 1.4.0.`

## Glossary

Keep a table of known mishearings in `templates/glossary.md` (or inline here) and extend it whenever a new one appears.
