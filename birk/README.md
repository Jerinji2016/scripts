# birk

A script for automating with Shorebird Code Push in Flutter Projects.

Know more about [Shorebird](https://docs.shorebird.dev/)

> __NOTE:__ Currently only support android

## 🤝 How to use?

Or How I use is...

Copy this script and add it to your root folder of Flutter Project with file named as `birk`.

> __NOTE:__ If you put a different file name. Use the below command accordingly by replacing `./birk` with `./your-file-name`.

## 💯 Usage

`./birk [patch|release] [dev|stage|prod]`

- patch: Creates a patch under the current app version number in provided env.

- release: Creates a release user for new app version in provided env.
  
  > __NOTE:__ When running `release` make sure you have updated version number in `pubspec.yaml`

***

### 💡 Good To Know

#### How I work with Flutter project?

- Maintain your enviromnent files as json in .env folder in your flutter root project.
- Each environment will have _\<env\>.json_ as in `dev.json` for development environment.
