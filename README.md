# Project Info Site

This is the main repository for Project Info Site.

## Contributing

Please read our [contributors' guide](contribute/project_submission.md) for details on how to publish your own project on the site.

## Building Locally

This site is built Jekyll: a static site generator written in Ruby. See the [Jekyll quick start guide](https://jekyllrb.com/docs/) for instructions on how to install Jekyll and it's dependencies on your device. You might also need to install [node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs).

Then clone this repository:

```sh
git clone https://github.com/UCLH-Foundry/uclh-research-discovery.git
```

And build and serve the site with:

```sh
bundle exec jekyll serve
```

## Building with Docker

Docker deployment files are provided to develop in environments where installing
Ruby is not possible.

The file `compose.yml` binds the project folder to the host mount point
`/opt/code`. This is done so Jekyll can detect changes in the local files and
rebuild the website.

1. Clone this repository
2. Copy `sample.env` to `.env` and update with your environment configuration.
3. Build and serve the site with:

   ```sh
   docker compose build
   docker compose run --rm web bundle install
   docker compose up
   ```

   The second command will install the Ruby dependencies in your local project
   folder and make them available for the Docker container during development.
