First off, thank you for considering contributing to PyHydra. It's people
like you that make PyHydra such a great tool.

# Where do I go from here?

If you've noticed a bug or have a feature request, notify us by creating an [issue][https://github.com/realvisiontv/PyHydra/issues/new]! It's
generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

If you have a general question about PyHydra, contact the maintainer.

## Clone & create a branch

If this is something you think you can fix, then clone PyHydra and create a branch with a descriptive name.

A good branch name would be (where issue #11 is the ticket you're working on):

```sh
git checkout -b 11-bug-fix
```

## Get the test suite running

We're using pytest to run our test cases. Note: test cases will be added in future releases of PyHydra

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first :smile_cat:

## View your changes

View your changes by testing your code against your local Confluent Cloud platform. The docker compose file to spin up your local Confluent Platform is provided in the project's root directory. All you need to do us run `docker-compose -f docker-compose-cp.yml up -d` to spin up Confluent Platform in your local environment

## Get the style right

We're using pylint linter to style our code base. Note: pylint lineter will be added in future releases of PyHydra

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with PyHydra's main branch:

```sh
git checkout main
git pull
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 11-bug-fix
git rebase master
git push --set-upstream origin 11-bug-fix
```

Finally, go to GitHub and [make a Pull Request][https://github.com/realvisiontv/PyHydra/pulls] :D

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

## Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

* It is passing CI.
* It has been approved by at least two maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
* It has no requested changes.
* It is up to date with current master

Any maintainer is allowed to merge a PR if all of these conditions are met.

