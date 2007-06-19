Name:           ragel   
Version:        5.22
Release:        1%{?dist}
Summary:        Finite state machine compiler

Group:          Development/Tools
License:        GPL 
URL:            http://www.cs.queensu.ca/~thurston/ragel/ 
Source0:        http://www.cs.queensu.ca/~thurston/ragel/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  transfig, tetex-latex
Requires:       gawk

Patch0:         ragel-Makefile-install.patch
Patch1:         ragel-rlcodegen-replace.patch

%description
Ragel compiles finite state machines from regular languages into executable C,
C++, Objective-C, or D code. Ragel state machines can not only recognize byte
sequences as regular expression machines do, but can also execute code at
arbitrary points in the recognition of a regular language. Code embedding is
done using inline operators that do not disrupt the regular language syntax.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%configure 
make %{?_smp_mflags}
pushd doc
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
make prefix=%{buildroot}%{_prefix} install
chmod a-x examples/*
pushd doc
make prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir} docdir=%{buildroot}%{_docdir}/%{name}-%{version} install
popd

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ragel.vim
%doc examples
%doc doc/ragel-guide.pdf
%{_bindir}/rlgen-ruby
%{_bindir}/rlgen-java
%{_bindir}/rlgen-dot
%{_bindir}/rlgen-cd
%{_bindir}/ragel
%{_mandir}/*/*

%changelog
* Mon Jun 18 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.22-1
- update to 5.22
- remove ragel-Makefile-in.patch - it was applied upstream
- update ragel-rlcodegen-replace.patch to apply cleanly

* Sat Mar 24 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-4
- further replacement of rlcodegen
- rework patches

* Fri Mar 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-3
- replace RPM_BUILD_ROOT in spec file with buildroot macro
- cleanup rpmlint errors for the src.rpm
- add ragel(1) man page patch

* Tue Mar 20 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 5.19-1
- Creation of spec file
