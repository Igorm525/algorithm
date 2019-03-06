var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var uglify = require('gulp-uglify');
var babel = require('gulp-babel');
var concat = require('gulp-concat');

gulp.task('default', function (callback) {
  return gulp.src(['node_modules/babel-polyfill/dist/polyfill.js', 'src/**/*.js'])
    .pipe(babel())
    // .pipe(uglify())
    .pipe(concat('index.js'))
    .pipe(gulp.dest('public'));
});


