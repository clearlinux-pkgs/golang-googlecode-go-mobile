Name     : golang-googlecode-go-mobile 
Version  : 0
Release  : 4
URL      : https://github.com/golang/mobile/archive/159023b6193b7d521d55cc5d9619278e2e1fd4a5.tar.gz
Source0  : https://github.com/golang/mobile/archive/159023b6193b7d521d55cc5d9619278e2e1fd4a5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go
BuildRequires : mesa-dev 

%description
Vendored copy of golang.org/x/tools/go/loader.
See vendor.bash.
Modifications:
- removed dependency on x/tools/astutil
- removed dependency on x/tools/buildutil
- uses Go 1.5's go/types package

%prep
%setup -q -n mobile-159023b6193b7d521d55cc5d9619278e2e1fd4a5

%build

%install
%global gopath /usr/lib/golang
%global library_path golang.org/x/mobile
rm -rf %{buildroot}
# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s h c golden; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

export GOPATH=%{buildroot}%{gopath}
go build golang.org/x/mobile/app

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/app
go test %{library_path}/bind
go test %{library_path}/cmd/gomobile
# requires openal library
# go test %{library_path}/exp/audio
go test %{library_path}/exp/f32
go test %{library_path}/exp/gl/glutil ||:


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/golang.org/x/mobile/app/android.c
/usr/lib/golang/src/golang.org/x/mobile/app/android.go
/usr/lib/golang/src/golang.org/x/mobile/app/app.go
/usr/lib/golang/src/golang.org/x/mobile/app/app_test.go
/usr/lib/golang/src/golang.org/x/mobile/app/darwin_amd64.go
/usr/lib/golang/src/golang.org/x/mobile/app/darwin_armx.go
/usr/lib/golang/src/golang.org/x/mobile/app/doc.go
/usr/lib/golang/src/golang.org/x/mobile/app/internal/apptest/apptest.go
/usr/lib/golang/src/golang.org/x/mobile/app/internal/callfn/callfn.go
/usr/lib/golang/src/golang.org/x/mobile/app/internal/callfn/callfn_arm.s
/usr/lib/golang/src/golang.org/x/mobile/app/internal/testapp/testapp.go
/usr/lib/golang/src/golang.org/x/mobile/app/x11.c
/usr/lib/golang/src/golang.org/x/mobile/app/x11.go
/usr/lib/golang/src/golang.org/x/mobile/asset/asset.go
/usr/lib/golang/src/golang.org/x/mobile/asset/asset_android.go
/usr/lib/golang/src/golang.org/x/mobile/asset/asset_darwin_armx.go
/usr/lib/golang/src/golang.org/x/mobile/asset/asset_desktop.go
/usr/lib/golang/src/golang.org/x/mobile/asset/doc.go
/usr/lib/golang/src/golang.org/x/mobile/bind/bind.go
/usr/lib/golang/src/golang.org/x/mobile/bind/bind_test.go
/usr/lib/golang/src/golang.org/x/mobile/bind/gengo.go
/usr/lib/golang/src/golang.org/x/mobile/bind/genjava.go
/usr/lib/golang/src/golang.org/x/mobile/bind/genobjc.go
/usr/lib/golang/src/golang.org/x/mobile/bind/java/doc.go
/usr/lib/golang/src/golang.org/x/mobile/bind/java/seq_android.c
/usr/lib/golang/src/golang.org/x/mobile/bind/java/seq_android.go
/usr/lib/golang/src/golang.org/x/mobile/bind/java/seq_android.h
/usr/lib/golang/src/golang.org/x/mobile/bind/java/seq_test.go
/usr/lib/golang/src/golang.org/x/mobile/bind/java/testpkg/testpkg.go
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/doc.go
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/seq.h
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/seq_darwin.go
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/test_main.go
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/testpkg/go_testpkg/go_testpkg.go
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/testpkg/objc_testpkg/GoTestpkg.h
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/testpkg/objc_testpkg/reference/GoTestpkg.h
/usr/lib/golang/src/golang.org/x/mobile/bind/objc/testpkg/testpkg.go
/usr/lib/golang/src/golang.org/x/mobile/bind/printer.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/buffer.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/ref.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/seq.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/seq_test.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/string.go
/usr/lib/golang/src/golang.org/x/mobile/bind/seq/string_test.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/basictypes.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/basictypes.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/basictypes.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/basictypes.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/basictypes.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/customprefix.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/customprefix.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/customprefix.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/customprefix.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/interfaces.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/interfaces.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/interfaces.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/interfaces.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/interfaces.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue10788.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue10788.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue10788.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue10788.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue10788.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12328.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12328.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12328.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12328.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12328.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12403.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12403.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12403.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12403.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/issue12403.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/structs.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/structs.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/structs.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/structs.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/structs.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/try.go
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/try.go.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/try.java.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/try.objc.h.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/testdata/try.objc.m.golden
/usr/lib/golang/src/golang.org/x/mobile/bind/types.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gobind/doc.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gobind/gen.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gobind/main.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/binary_xml.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/binary_xml_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/bind.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/bind_androidapp.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/bind_iosapp.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/bind_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/build.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/build_androidapp.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/build_darwin_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/build_iosapp.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/build_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/cert.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/cert_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/dex.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/doc.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/env.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/gendex.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/hashes.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/init.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/init_test.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/install.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/main.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/manifest.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/release.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/strings_flag.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/version.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/writer.go
/usr/lib/golang/src/golang.org/x/mobile/cmd/gomobile/writer_test.go
/usr/lib/golang/src/golang.org/x/mobile/event/key/code_string.go
/usr/lib/golang/src/golang.org/x/mobile/event/key/key.go
/usr/lib/golang/src/golang.org/x/mobile/event/lifecycle/lifecycle.go
/usr/lib/golang/src/golang.org/x/mobile/event/mouse/mouse.go
/usr/lib/golang/src/golang.org/x/mobile/event/paint/paint.go
/usr/lib/golang/src/golang.org/x/mobile/event/size/size.go
/usr/lib/golang/src/golang.org/x/mobile/event/touch/touch.go
/usr/lib/golang/src/golang.org/x/mobile/example/audio/main.go
/usr/lib/golang/src/golang.org/x/mobile/example/audio/main_x.go
/usr/lib/golang/src/golang.org/x/mobile/example/basic/main.go
/usr/lib/golang/src/golang.org/x/mobile/example/basic/main_x.go
/usr/lib/golang/src/golang.org/x/mobile/example/bind/hello/hello.go
/usr/lib/golang/src/golang.org/x/mobile/example/bind/ios/bind/AppDelegate.h
/usr/lib/golang/src/golang.org/x/mobile/example/bind/ios/bind/ViewController.h
/usr/lib/golang/src/golang.org/x/mobile/example/ivy/ios/ivy/AppDelegate.h
/usr/lib/golang/src/golang.org/x/mobile/example/ivy/ios/ivy/DocsController.h
/usr/lib/golang/src/golang.org/x/mobile/example/ivy/ios/ivy/IvyController.h
/usr/lib/golang/src/golang.org/x/mobile/example/ivy/ios/ivy/Suggestion.h
/usr/lib/golang/src/golang.org/x/mobile/example/network/main.go
/usr/lib/golang/src/golang.org/x/mobile/example/network/main_x.go
/usr/lib/golang/src/golang.org/x/mobile/example/sprite/main.go
/usr/lib/golang/src/golang.org/x/mobile/example/sprite/main_x.go
/usr/lib/golang/src/golang.org/x/mobile/exp/app/debug/fps.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/al.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/al_android.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/al_notandroid.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/alc.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/alc_android.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/alc_notandroid.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/al/const.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/audio.go
/usr/lib/golang/src/golang.org/x/mobile/exp/audio/audio_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/affine.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/affine_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/f32.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/f32_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/gen.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/mat3.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/mat4.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/table.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/vec3.go
/usr/lib/golang/src/golang.org/x/mobile/exp/f32/vec4.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/doc.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/font.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/font_android.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/font_darwin.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/font_linux.go
/usr/lib/golang/src/golang.org/x/mobile/exp/font/font_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/context_darwin_amd64.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/context_x11.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/doc.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/glimage.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/glimage_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/gl/glutil/glutil.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sensor/android.c
/usr/lib/golang/src/golang.org/x/mobile/exp/sensor/android.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sensor/darwin_armx.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sensor/notmobile.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sensor/sensor.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/clock/clock.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/clock/tween.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/clock/tween_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/glsprite/glsprite.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/portable/affine_test.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/portable/portable.go
/usr/lib/golang/src/golang.org/x/mobile/exp/sprite/sprite.go
/usr/lib/golang/src/golang.org/x/mobile/geom/geom.go
/usr/lib/golang/src/golang.org/x/mobile/gl/consts.go
/usr/lib/golang/src/golang.org/x/mobile/gl/doc.go
/usr/lib/golang/src/golang.org/x/mobile/gl/gendebug.go
/usr/lib/golang/src/golang.org/x/mobile/gl/gl.go
/usr/lib/golang/src/golang.org/x/mobile/gl/gldebug.go
/usr/lib/golang/src/golang.org/x/mobile/gl/interface.go
/usr/lib/golang/src/golang.org/x/mobile/gl/types_debug.go
/usr/lib/golang/src/golang.org/x/mobile/gl/types_prod.go
/usr/lib/golang/src/golang.org/x/mobile/gl/work.c
/usr/lib/golang/src/golang.org/x/mobile/gl/work.go
/usr/lib/golang/src/golang.org/x/mobile/gl/work.h
/usr/lib/golang/src/golang.org/x/mobile/internal/loader/cgo.go
/usr/lib/golang/src/golang.org/x/mobile/internal/loader/loader.go
/usr/lib/golang/src/golang.org/x/mobile/internal/loader/util.go
/usr/lib/golang/src/golang.org/x/mobile/internal/mobileinit/ctx_android.go
/usr/lib/golang/src/golang.org/x/mobile/internal/mobileinit/mobileinit.go
/usr/lib/golang/src/golang.org/x/mobile/internal/mobileinit/mobileinit_android.go
/usr/lib/golang/src/golang.org/x/mobile/internal/mobileinit/mobileinit_ios.go
