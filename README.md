# gradle-helper
the Android Studio use gradle as building tool. the Studio(and same to IntelliJ with gradle plugin) got stuck when you switch between projects. because of downloading the new gradle version. if internet connection to the gradle repository is slow, cache all version pre-head is a good idea

where to cache to? inspired by this blog post:
  http://www.liudonghua.com/?p=380


## Usage
download versions you want from:
  https://services.gradle.org/distributions

```
main.py <zip_dir> <glob_*>   copy pattern matched zip files
main.py <zip_dir>            copy gradle*.zip in <zip_dir>
```
* zip_dir, the dir you push you downloaded gradle zip to with other quicker way.
* glob_*,  you might want to copy specific version
