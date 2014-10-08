#BVBootstrap

##A BV-specific version of [Bootstrap](https://s3.amazonaws.com/bv-bootstrap/v3.2.0/docs/getting-started/index.html)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](http://twitter.com/mdo) and [Jacob Thornton](http://twitter.com/fat), and maintained by the [core team](https://github.com/twbs?tab=members) with the massive support and involvement of the community.
BVBootstrap builds off of Bootstrap's functionality and provides BV-specific formatting, components, and javascript.

## Table of contents
 - [Quick Start] (#quick-start)
 - [Project Structure](#project-structure)
 - [Compiling CSS and JavaScript](#compiling-css-and-javascript)
 - [Contributing](#contributing)
 - [Versioning](#versioning)
 - [Copyright and license](#copyright-and-license)


## Quick Start
1. Clone the repo: `git clone git://github.com/bazaarvoice/bvbootstrap.git`.
2. Run `bower install bootstrap` in the root `/bvbootstrap` directory.
3. Install `grunt-cli` globally with `npm install -g grunt-cli`.
4. Navigate to the root `/bvbootstrap` directory, then run `npm install`. npm will look at [package.json](https://github.com/bazaarvoice/bvbootstrap/blob/master/package.json) and automatically install the necessary local dependencies listed there.
5. Run `grunt` from the root `/bvbootstrap` directory to build and compile the project.
6. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v1.x).
7. From the root `/bvbootstrap` directory, run `jekyll serve` in the command line.
8. Open <http://localhost:9001> in your browser, and voilà.


## Project Structure
The project has been structured so that updating to a new version of Bootstrap is as easy as possible.  The defaultBootstrap directory contains a completely
unmodified copy of Twitter Bootstrap, to use as a base.  This is compiled first.  The custom directory includes custom LESS, js, and font files that override
Bootstrap's defaults.  The directory is set up like this:
```
bvbootstrap/
├── custom/
│   ├── fonts/
│   ├── js/
│   ├── less/
│   └── lessIcons/
|
├── defaultBootstrap/
│   
└── docs/
│    
└── ...etc
```

## Compiling CSS and JavaScript

Bootstrap uses [Grunt](http://gruntjs.com/) with convenient methods for working with the framework. It's how we compile our code, run tests, and more. To use it, install the required dependencies as directed and then run some Grunt commands.

### Install Grunt

From the command line:

1. Install `grunt-cli` globally with `npm install -g grunt-cli`.
2. Navigate to the root `/bootstrap` directory, then run `npm install`. npm will look at [package.json](https://github.com/bazaarvoice/bvbootstrap/blob/master/package.json) and automatically install the necessary local dependencies listed there.

When completed, you'll be able to run the various Grunt commands provided from the command line.

**Unfamiliar with `npm`? Don't have node installed?** That's a-okay. npm stands for [node packaged modules](http://npmjs.org/) and is a way to manage development dependencies through node.js. [Download and install node.js](http://nodejs.org/download/) before proceeding.

### Available Grunt commands

#### Build - `grunt`
Run `grunt` to run tests locally and compile the CSS and JavaScript into `/dist`. **Uses [Less](http://lesscss.org/) and [UglifyJS](http://lisperator.net/uglifyjs/).**

#### Only compile CSS and JavaScript - `grunt dist`
`grunt dist` creates the `/dist` directory with compiled files. **Uses [Less](http://lesscss.org/) and [UglifyJS](http://lisperator.net/uglifyjs/).**

#### Tests - `grunt test`
Runs [JSHint](http://jshint.com) and [QUnit](http://qunitjs.com/) tests headlessly in [PhantomJS](http://phantomjs.org/) (used for CI).

#### Watch - `grunt watch`
This is a convenience method for watching just Less files and automatically building them whenever you save.

### Troubleshooting dependencies

Should you encounter problems with installing dependencies or running Grunt commands, uninstall all previous dependency versions (global and local). Then, rerun `npm install`.



## Contributing

Please read through our [contributing guidelines](https://github.com/bazaarvoice/bvbootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, BVBootstrap is maintained under the Semantic Versioning guidelines. Sometimes we screw up, but we'll adhere to these rules whenever possible.

Releases will be numbered with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

- Breaking backward compatibility **bumps the major** while resetting minor and patch
- New additions without breaking backward compatibility **bumps the minor** while resetting the patch
- Bug fixes and misc changes **bumps only the patch**

For more information on SemVer, please visit <http://semver.org/>.


## Copyright and license

Twitter Bootstrap Code and documentation copyright 2011-2014 Twitter, Inc. Code released under [the MIT license](LICENSE). Docs released under [Creative Commons](docs/LICENSE).
