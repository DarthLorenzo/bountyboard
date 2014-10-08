/*!
 * Bootstrap's Gruntfile
 * http://getbootstrap.com
 * Copyright 2013-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

module.exports = function (grunt) {
  'use strict';

  // Force use of Unix newlines
  grunt.util.linefeed = '\n';

  RegExp.quote = function (string) {
    return string.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&');
  };

  var fs = require('fs');
  var path = require('path');
  var npmShrinkwrap = require('npm-shrinkwrap');
  var generateGlyphiconsData = require('./grunt/bs-glyphicons-data-generator.js');
  var BsLessdocParser = require('./grunt/bs-lessdoc-parser.js');
  var generateRawFilesJs = require('./grunt/bs-raw-files-generator.js');

  // Project configuration.
  grunt.initConfig({

    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    bower: grunt.file.readJSON('bower.json'),
    banner: '/*!\n' +
            ' * Bootstrap v<%= pkg.version %> (<%= pkg.homepage %>)\n' +
            ' * Copyright 2011-<%= grunt.template.today("yyyy") %> <%= pkg.author %>\n' +
            ' * Licensed under <%= pkg.license.type %> (<%= pkg.license.url %>)\n' +
            ' */\n',
    jqueryCheck: 'if (typeof jQuery === \'undefined\') { throw new Error(\'Bootstrap\\\'s JavaScript requires jQuery\') }\n\n',

    // Task configuration.
    clean: {
      dist: ['dist', 'docs/dist']
    },

    jshint: {
      options: {
        jshintrc: 'defaultBootstrap/js/.jshintrc'
      },
      grunt: {
        options: {
          jshintrc: 'defaultBootstrap/grunt/.jshintrc'
        },
        src: ['Gruntfile.js', 'defaultBootstrap/grunt/*.js']
      },
      src: {
        src: 'defaultBootstrap/js/*.js'
      },
      test: {
        options: {
          jshintrc: 'defaultBootstrap/js/tests/unit/.jshintrc'
        },
        src: 'defaultBootstrap/js/tests/unit/*.js'
      },
      assets: {
        src: ['docs/assets/js/_src/application.js', 'docs/assets/js/_src/customizer.js']
      }
    },

    jscs: {
      options: {
        config: 'defaultBootstrap/js/.jscsrc'
      },
      grunt: {
        src: ['Gruntfile.js', 'defaultBootstrap/grunt/*.js']
      },
      src: {
        src: 'defaultBootstrap/js/*.js'
      },
      test: {
        src: 'defaultBootstrap/js/tests/unit/*.js'
      },
      assets: {
        options: {
          requireCamelCaseOrUpperCaseIdentifiers: null
        },
        src: '<%= jshint.assets.src %>'
      }
    },

    csslint: {
      options: {
        csslintrc: 'custom/less/.csslintrc'
      },
      src: [
        'dist/css/bvbootstrap.css',
        'dist/css/bootstrap-theme.css',
        'docs/assets/css/docs.css',
        'docs/examples/**/*.css'
      ]
    },

    concat: {
      options: {
        banner: '<%= banner %>\n<%= jqueryCheck %>',
        stripBanners: false
      },
      bootstrap: {
        src: [
          'defaultBootstrap/js/transition.js',
          'defaultBootstrap/js/alert.js',
          'defaultBootstrap/js/button.js',
          'defaultBootstrap/js/carousel.js',
          'defaultBootstrap/js/collapse.js',
          'defaultBootstrap/js/dropdown.js',
          'defaultBootstrap/js/modal.js',
          'defaultBootstrap/js/tooltip.js',
          'defaultBootstrap/js/popover.js',
          'defaultBootstrap/js/scrollspy.js',
          'defaultBootstrap/js/tab.js',
          'defaultBootstrap/js/affix.js',
          'custom/js/typeahead.js',
          'custom/js/ratings.js'
        ],
        dest: 'dist/js/<%= pkg.name %>.js'
      }
    },

    uglify: {
      options: {
        report: 'min'
      },
      bootstrap: {
        options: {
          banner: '<%= banner %>'
        },
        src: '<%= concat.bootstrap.dest %>',
        dest: 'dist/js/<%= pkg.name %>.min.js'
      },
      customize: {
        options: {
          preserveComments: 'some'
        },
        src: [
          'docs/assets/js/vendor/less.min.js',
          'docs/assets/js/vendor/jszip.min.js',
          'docs/assets/js/vendor/uglify.min.js',
          'docs/assets/js/vendor/blob.js',
          'docs/assets/js/vendor/filesaver.js',
          'docs/assets/js/raw-files.min.js',
          'docs/assets/js/_src/customizer.js'
        ],
        dest: 'docs/assets/js/customize.min.js'
      },
      docsJs: {
        options: {
          preserveComments: 'some'
        },
        src: [
          'docs/assets/js/vendor/holder.js',
          'docs/assets/js/_vendor/ZeroClipboard.min.js',
          'docs/assets/js/_src/application.js',
          'docs/assets/js/_src/typeahead-demo.js'
        ],
        dest: 'docs/assets/js/docs.min.js'
      }
    },

    less: {
      compileBVGlyphs: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'bvglyphs.css.map',
          sourceMapFilename: 'dist/css/bvglyphs.css.map'
        },
        files: {
          'dist/css/bvglyphs.css': 'custom/lessIcons/customBVGlyphs.less'
        }
      },
      compileBVGlyphsIE7Icons: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'bvglyphs-ie7.css.map',
          sourceMapFilename: 'dist/css/bvglyphs-ie7.css.map'
        },
        files: {
          'dist/css/bvglyphs-ie7.css': 'custom/lessIcons/customBVGlyphsIE7.less'
        }
      },
      compilePictos: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'pictos.css.map',
          sourceMapFilename: 'dist/css/pictos.css.map'
        },
        files: {
          'dist/css/pictos.css': 'custom/lessIcons/customPictos.less'
        }
      },
      compilePictosIE7: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'pictos-ie7.css.map',
          sourceMapFilename: 'dist/css/pictos-ie7.css.map'
        },
        files: {
          'dist/css/pictos-ie7.css': 'custom/lessIcons/customPictosIE7.less'
        }
      },
      compileFontAwesome: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'fontawesome.css.map',
          sourceMapFilename: 'dist/css/fontawesome.css.map'
        },
        files: {
          'dist/css/fontawesome.css': 'custom/lessIcons/customFontAwesomeIcons.less'
        }
      },
      compileFontAwesomeIE7: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'fontawesome-ie7.css.map',
          sourceMapFilename: 'dist/css/fontawesome-ie7.css.map'
        },
        files: {
          'dist/css/fontawesome-ie7.css': 'custom/lessIcons/customFontAwesomeIconsIE7.less'
        }
      },
      compileCore: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: '<%= pkg.name %>.css.map',
          sourceMapFilename: 'dist/css/<%= pkg.name %>.css.map'
        },
        files: {
          'dist/css/<%= pkg.name %>.css': 'custom/less/customBootstrap.less'
        }
      },
      compileTheme: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: '<%= pkg.name %>-theme.css.map',
          sourceMapFilename: 'dist/css/<%= pkg.name %>-theme.css.map'
        },
        files: {
          'dist/css/<%= pkg.name %>-theme.css': 'defaultBootstrap/less/theme.less'
        }
      },
      minify: {
        options: {
          cleancss: true,
          report: 'min'
        },
        files: {
          'dist/css/<%= pkg.name %>.min.css': 'dist/css/<%= pkg.name %>.css',
          'dist/css/<%= pkg.name %>-theme.min.css': 'dist/css/<%= pkg.name %>-theme.css',
          'dist/css/bvglyphs.min.css': 'dist/css/bvglyphs.css',
          'dist/css/fontawesome.min.css': 'dist/css/fontawesome.css',
//          removing the following two lines because less compiler is confused about expression()
//          'dist/css/bvglyphs-ie7.min.css': 'dist/css/bvglyphs-ie7.css',
//          'dist/css/pictos-ie7.min.css': 'dist/css/pictos-ie7.css',
//          'dist/css/fontawesome-ie7.min.css': 'dist/css/fontawesome-ie7.css',
          'dist/css/pictos.min.css': 'dist/css/pictos.css'
        }
      }
    },

    cssmin: {
      compress: {
        options: {
          keepSpecialComments: '*',
          noAdvanced: true, // turn advanced optimizations off until the issue is fixed in clean-css
          report: 'min',
          selectorsMergeMode: 'ie8'
        },
        src: [
          'docs/assets/css/docs.css',
          'docs/assets/css/pygments-manni.css'
        ],
        dest: 'docs/assets/css/docs.min.css'
      }
    },

    usebanner: {
      dist: {
        options: {
          position: 'top',
          banner: '<%= banner %>'
        },
        files: {
          src: [
            'dist/css/<%= pkg.name %>.css',
            'dist/css/<%= pkg.name %>.min.css',
            'dist/css/<%= pkg.name %>-theme.css',
            'dist/css/<%= pkg.name %>-theme.min.css'
          ]
        }
      }
    },

    csscomb: {
      options: {
        config: 'less/.csscomb.json'
      },
      dist: {
        files: {
          'dist/css/<%= pkg.name %>.css': 'dist/css/<%= pkg.name %>.css',
          'dist/css/<%= pkg.name %>-theme.css': 'dist/css/<%= pkg.name %>-theme.css',
          'dist/css/bvglyphs.css': 'dist/css/bvglyphs.css',
          'dist/css/bvglyphs-ie7.css': 'dist/css/bvglyphs-ie7.css',
          'dist/css/pictos.css': 'dist/css/pictos.css',
          'dist/css/pictos-ie7.css': 'dist/css/pictos-ie7.css'
        }
      },
      examples: {
        expand: true,
        cwd: 'docs/examples/',
        src: ['**/*.css'],
        dest: 'docs/examples/'
      }
    },

    copy: {
      fonts: {
        expand: true,
        src: ['defaultBootstrap/fonts/*',
        'custom/fonts/*'],
        dest: 'dist/fonts/',
        flatten: true
      },
      docs: {
        expand: true,
        cwd: './dist',
        src: [
          '{css,js}/*.min.*',
          'css/*.map',
          'fonts/*'
        ],
        dest: 'docs/dist'
      }
    },

    qunit: {
      options: {
        inject: 'defaultBootstrap/js/tests/unit/phantom.js'
      },
      files: 'defaultBootstrap/js/tests/index.html'
    },

    connect: {
      server: {
        options: {
          port: 3000,
          base: '.'
        }
      }
    },

    jekyll: {
      docs: {}
    },

    jade: {
      compile: {
        options: {
          pretty: true,
          data: function () {
            var filePath = path.join(__dirname, 'custom/less/customVariables.less');
            var fileContent = fs.readFileSync(filePath, { encoding: 'utf8' });
            var parser = new BsLessdocParser(fileContent);
            return { sections: parser.parseFile() };
          }
        },
        files: {
          'docs/_includes/customizer-variables.html': 'docs/jade/customizer-variables.jade',
          'docs/_includes/nav-customize.html': 'docs/jade/customizer-nav.jade'
        }
      }
    },

    validation: {
      options: {
        charset: 'utf-8',
        doctype: 'HTML5',
        failHard: true,
        reset: true,
        relaxerror: [
          'Bad value X-UA-Compatible for attribute http-equiv on element meta.',
          'Element img is missing required attribute src.'
        ]
      },
      files: {
        src: '_gh_pages/**/*.html'
      }
    },

    watch: {
      src: {
        files: '<%= jshint.src.src %>',
        tasks: ['jshint:src', 'qunit']
      },
      test: {
        files: '<%= jshint.test.src %>',
        tasks: ['jshint:test', 'qunit']
      },
      less: {
        files: 'custom/less/*.less',
        tasks: 'less'
      }
    },

    sed: {
      versionNumber: {
        pattern: (function () {
          var old = grunt.option('oldver');
          return old ? RegExp.quote(old) : old;
        })(),
        replacement: grunt.option('newver'),
        recursive: true
      }
    },

    'saucelabs-qunit': {
      all: {
        options: {
          build: process.env.TRAVIS_JOB_ID,
          concurrency: 10,
          urls: ['http://127.0.0.1:3000/js/tests/index.html'],
          browsers: grunt.file.readYAML('defaultBootstrap/grunt/sauce_browsers.yml')
        }
      }
    },

    exec: {
      npmUpdate: {
        command: 'npm update'
      },
      npmShrinkWrap: {
        command: 'npm shrinkwrap --dev'
      }
    },

    s3: {
      options: {
        access: 'public-read',
        bucket: 'bv-bootstrap'
      },
      release: {
        upload: [
          {
            src: 'dist/**/*',
            rel: 'dist',
            dest: 'v<%= bower.version %>/dist'
          }
        ]
      },
      docs: {
        upload: [
          {
            src: '_gh_pages/**/*',
            rel: '_gh_pages',
            dest: 'v<%= bower.version %>/docs/'
          },
          {
            src: '_gh_pages/assets/**',
            rel: '_gh_pages/assets',
            dest: 'v<%= bower.version %>/assets'
          }
        ]
      }
    }
  });


  // These plugins provide necessary tasks.
  require('load-grunt-tasks')(grunt, { scope: 'devDependencies' });

  // Docs HTML validation task
  grunt.registerTask('validate-html', ['jekyll', 'validation']);

  // Test task.
  var testSubtasks = [];
  // Skip core tests if running a different subset of the test suite
  if (!process.env.TWBS_TEST || process.env.TWBS_TEST === 'core') {
    testSubtasks = testSubtasks.concat(['dist-css', 'csslint', 'jshint', 'jscs', 'qunit', 'build-customizer-html']);
  }
  // Skip HTML validation if running a different subset of the test suite
  if (!process.env.TWBS_TEST || process.env.TWBS_TEST === 'validate-html') {
    testSubtasks.push('validate-html');
  }
  // Only run Sauce Labs tests if there's a Sauce access key
  if (typeof process.env.SAUCE_ACCESS_KEY !== 'undefined' &&
      // Skip Sauce if running a different subset of the test suite
      (!process.env.TWBS_TEST || process.env.TWBS_TEST === 'sauce-js-unit')) {
    testSubtasks.push('connect');
    testSubtasks.push('saucelabs-qunit');
  }
  grunt.registerTask('test', testSubtasks);

  // JS distribution task.
  grunt.registerTask('dist-js', ['concat', 'uglify']);

  // CSS distribution task.
  grunt.registerTask('dist-css', ['less', 'cssmin', 'csscomb', 'usebanner']);

  // Docs distribution task.
  grunt.registerTask('dist-docs', 'copy:docs');

  // Full distribution task.
  grunt.registerTask('dist', ['clean', 'dist-css', 'copy:fonts', 'dist-js', 'dist-docs']);

  // Default task.
  grunt.registerTask('default', ['test', 'dist', 'build-glyphicons-data', 'build-customizer', 'update-shrinkwrap']);

  // Version numbering task.
  // grunt change-version-number --oldver=A.B.C --newver=X.Y.Z
  // This can be overzealous, so its changes should always be manually reviewed!
  grunt.registerTask('change-version-number', 'sed');

  grunt.registerTask('build-glyphicons-data', generateGlyphiconsData);

  // task for building customizer
  grunt.registerTask('build-customizer', ['build-customizer-html', 'build-raw-files']);
  grunt.registerTask('build-customizer-html', 'jade');
  grunt.registerTask('build-raw-files', 'Add scripts/less files to customizer.', function () {
    var banner = grunt.template.process('<%= banner %>');
    generateRawFilesJs(banner);
    return;
  });
  // Task for updating the cached npm packages used by the Travis build (which are controlled by test-infra/npm-shrinkwrap.json).
  // This task should be run and the updated file should be committed whenever Bootstrap's dependencies change.
  grunt.registerTask('update-shrinkwrap', ['exec:npmUpdate', '_update-shrinkwrap']);
  grunt.registerTask('_update-shrinkwrap', function () {
    var done = this.async();
    npmShrinkwrap({ dev: true, dirname: __dirname }, function (err) {
      if (err) {
        grunt.fail.warn(err)
      }
      var dest = 'test-infra/npm-shrinkwrap.json';
      fs.renameSync('npm-shrinkwrap.json', dest);
      grunt.log.writeln('File ' + dest.cyan + ' updated.');
      done();
    });
  });
};
