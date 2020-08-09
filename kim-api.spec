Name:                kim-api
Version:             2.1.3
%global sover   2
Release:             1
Summary:             Open Knowledgebase of Interatomic Models KIM API
License:             CDDL-1.0
Url:                 https://www.openkim.org
Source0:             https://s3.openkim.org/kim-api/kim-api-%{version}.txz
BuildRequires:       gcc-c++ gcc-gfortran pkgconfig bash-completion
%global b_compdir %(pkg-config --variable=completionsdir bash-completion)
%if "%{b_compdir}" == ""
%global b_compdir /etc/bash_completion.d
%endif
%global z_compdir %{_datadir}/zsh/site-functions
BuildRequires:       cmake3 >= 3.4 vim
%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.
This package can be used to load all the files (libraries, headers, and
documentation) for the KIM-API.

%package devel
Summary:             Development headers and libraries for kim-api
Requires:            %{name} = %{version}-%{release}
%description devel
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.
This package contains the development files (headers and documentation) for the
KIM-API.

%package examples
Summary:             Example models for kim-api
Requires:            %{name} = %{version}-%{release}
%description examples
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.
This package contains the example models for the KIM-API.

%prep
%setup -q

%build
mkdir build
pushd build
%{cmake3} -DCMAKE_SKIP_RPATH=ON -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} -DBASH_COMPLETION_COMPLETIONSDIR=%{b_compdir} -DZSH_COMPLETION_COMPLETIONSDIR=%{z_compdir} ..
%make_build

%install
%make_install -C build
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
mv %{buildroot}/usr/share/emacs/site-lisp/kim-api/kim-api-c-style.el %{buildroot}%{_datadir}/emacs/site-lisp/kim-api-c-style.el
%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.CDDL
%{_bindir}/kim-api-*
%dir %{_libexecdir}/kim-api
%{_libexecdir}/kim-api/kim-api-collections-info
%{_libexecdir}/kim-api/kim-api-simulator-model
%{_libexecdir}/kim-api/kim-api-shared-library-test
%{_libdir}/libkim-api.so.%{sover}
%{b_compdir}/kim-api-collections-management.bash
%{z_compdir}/_kim-api-collections-management
%{z_compdir}/kim-api-collections-management.bash
%{_datadir}/emacs/site-lisp/kim-api-c-style.el

%files devel
%{_includedir}/kim-api/
%{_libdir}/kim-api/mod/
%{_libdir}/kim-api/cmake/
%{_datadir}/cmake/
%dir %{_libdir}/kim-api/
%{_libdir}/libkim-api.so
%{_libdir}/pkgconfig/libkim-api.pc

%files examples
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/portable-models/
%{_libdir}/kim-api/simulator-models/

%changelog
* Mon Jul 27 2020 zhanghua <zhanghua40@huawei.com> - 2.1.3-1
- package init
