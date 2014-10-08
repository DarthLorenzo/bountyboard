# Working on BVBootstrap

Looking to contribute something to BVBootstrap? **Here's how you can help.**

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this open source project. In return,
they should reciprocate that respect in addressing your issue or assessing
patches and features.

##Writing Code

The BVBootstrap project directory was designed to make customization as easy as possible.  As a result, ALL changes (less, js, fonts, icons, etc.)
should be made in the `custom` directory.  **NEVER modify `defaultBootstrap`.**  

###Less Files

To add a .less file, create a new file in the `bvbootstrap/custom/less` directory.  Then modify `customBootstrap.less` to include your file.  That's all you have to do!

###JS Files

Adding .js files is a little more complicated.  To add a .js file, create a new file in the `bvbootstrap/custom/js` directory.  Then modify `bvbootstrap/Gruntfile.js` to add your file to the list of 
`src` files under `concat->bootstrap` (search around line 104).  This adds your js file to the list of js files compiled into bvbootstrap.min.js.

###Font Files

To add a font, first add .eot, .svg, .ttf, and .woff files to `bvbootstrap/custom/fonts`.  The modify `bvbootstrap/custom/less/customFonts.less` to include an 
`@font-face` annotation for your new font (follow the same format as the rest of the fonts listed there).  

###Icons

To add an icons font, there are a few steps.  First, add .eot, .svg, .ttf, and .woff files to `bvbootstrap/custom/fonts`.  Then add imports to your new icon files in 
`bvbootstrap/custom/customIcons.less` (this is a dependency on the `dist` directory; the first time you try to add your files, there won't be any css files there 
and your editor could throw an error.  That's ok-- just compile your code and this should get resolved automatically when the css files are generated).  Next, 
create a .less file for your icons in `bvbootstrap/custom/lessIcons` modelled off of any of the other files in that directory.
  Then, you'll need to add a task for compiling your font to
`bvbootstrap/Gruntfile.js` under the `less` task (look around line 207 for other icon examples, like font-awesome and pictos). Finally, you'll need to 
modify the minify task to also minify your icon files (look around line 263 to see how bvglyphs and fontawesome are set up).

##Modifying the Docs

The BVBootstrap docs (found in `bvbootstrap/docs`) are a great way to test your code after you've written a new feature.  It's important to keep the docs up-to-date
so BVBootstrap users know which cool features are available to them to use.  Begin by adding your feature to the CSS, Components, or Javascript html pages (found in `bvbootstrap/docs`).
Follow the layout of the other elements on the page.  Next, modify the corresponding nav file in `bvbootstrap/docs/_includes` so that the affix navigation
on the page includes your new feature.  If you need to make css changes to the docs, these are done in `bvbootstrap/docs/assets/docs.css` (docs.min.css will be created automatically, so don't
modify that).  If you also need to make javascript changes, you can either add your javascript snippet to `bvbootstrap/docs/assets/js/application.js` or create a separate javascript file in 
`bvbootstrap/docs/assets/js/_src`.  If you create a separate file, however, you'll need to modify the `docsJS` task in `bvbootstrap/Gruntfile.js` to include your new file (look around line 152 for how `typeahead-demo.js` is included). 
Then build the project and run the server to observe the results!

##Contributing Code

Please submit all pull requests against *-wip branches. 
If your pull request contains javascript patches or features, you must include relevant unit tests. Thanks!


##Bug tracker

Have a bug?

Enter **Bugs**, **Feature Requests**, or **Contribution enquiries** [here](https://github.com/bazaarvoice/bvbootstrap/issues).

##Upgrading

BVBootstrap's project structure was designed to make upgrading a breeze.  To upgrade to a newer version of Twitter Bootstrap, 
simply drop a new copy of the complete Bootstrap project into the defaultBootstrap directory.  The Gruntfile.js script knows which files to
override and where to expect Bootstrap dependencies.  

Occasionally, Bootstrap will change their dependencies.  In this case, you'll probably be able to
simply replace the  `"devDependencies"` portion of `bvbootstrap/package.js` with the new dependencies.

If a new feature is added, you'll need to update the docs (`bvbootstrap/docs`) to include it (see above).  