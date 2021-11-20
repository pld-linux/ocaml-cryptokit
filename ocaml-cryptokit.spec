# TODO: unity dll*stubs.so location to %{_libdir}/ocaml/stublibs?
#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Cryptographic toolkit for OCaml
Summary(pl.UTF-8):	Biblioteka kryptograficzna dla OCamla
Name:		ocaml-cryptokit
Version:	1.16.1
%define		verrel release%(echo %{version} | tr -d .)
Release:	3
License:	LGPL v2 with linking exception
Group:		Libraries
Source0:	https://github.com/xavierleroy/cryptokit/archive/%{verrel}/cryptokit-%{version}.tar.gz
# Source0-md5:	18591fc3f467bc33681be2cede36b8f1
URL:		http://pauillac.inria.fr/~xleroy/software.html#cryptokit
BuildRequires:	ocaml >= 1:3.09.2
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-dune-devel
BuildRequires:	ocaml-zarith
BuildRequires:	ocaml-zarith-devel
BuildRequires:	zlib-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include: symmetric-key cryptography: AES, DES, Triple-DES, ARCfour, in
ECB, CBC, CFB and OFB modes; public-key cryptography: RSA; hash
functions and MACs: SHA-1, MD5, and MACs based on AES and DES; random
number generation; encodings and compression: base 64, hexadecimal,
Zlib compression.

This package contains files needed to run bytecode executables using
this library.

%description -l pl.UTF-8
Biblioteka Cryptokit dostarcza szeroką gamę funkcji kryptograficznych,
które mogą być użyte w implementacji protokołów kryptograficznych w
aplikacjach, dla których ważne jest bezpieczeństwo. Dostarczane
funkcje to: szyfry symetryczne: AES, DES, 3DES, ARCFour w trybach ECB,
CBC, CFB oraz OFB; szyfr z kluczem publicznym RSA; kryptograficzne
funkcje skrótu i MACi: SHA-1, MD5 oraz MACi bazowane na AES oraz DES;
generacje liczb losowych; kodowania i kompresja: base 64, szesnastkowa
oraz zlib.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package devel
Summary:	Cryptographic toolkit for OCaml - development part
Summary(pl.UTF-8):	Biblioteka kryptograficzna dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq ocaml

%description devel
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include: symmetric-key cryptography: AES, DES, Triple-DES, ARCfour, in
ECB, CBC, CFB and OFB modes; public-key cryptography: RSA; hash
functions and MACs: SHA-1, MD5, and MACs based on AES and DES; random
number generation; encodings and compression: base 64, hexadecimal,
Zlib compression.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Biblioteka Cryptokit dostarcza szeroką gamę funkcji kryptograficznych,
które mogą być użyte w implementacji protokołów kryptograficznych w
aplikacjach, dla których ważne jest bezpieczeństwo. Dostarczane
funkcje to: szyfry symetryczne: AES, DES, 3DES, ARCFour w trybach ECB,
CBC, CFB oraz OFB; szyfr z kluczem publicznym RSA; kryptograficzne
funkcje skrótu i MACi: SHA-1, MD5 oraz MACi bazowane na AES oraz DES;
generacje liczb losowych; kodowania i kompresja: base 64, szesnastkowa
oraz zlib.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q -n cryptokit-%{verrel}

%build
dune build %{?_smp_mflags} @install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit

dune install --destdir=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir}/ocaml -name \*.ml -delete

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r test/*.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README.md
%dir %{_libdir}/ocaml/cryptokit
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllcryptokit_stubs.so
%{_libdir}/ocaml/cryptokit/cryptokit*.cma
%{_libdir}/ocaml/cryptokit/cryptokit*.cmi
%{_libdir}/ocaml/cryptokit/cryptokit*.cmt
%{_libdir}/ocaml/cryptokit/cryptokit*.cmti
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/cryptokit/cryptokit.cmxs
%endif
%{_libdir}/ocaml/cryptokit/META

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/cryptokit/cryptokit.cmi
%{_libdir}/ocaml/cryptokit/libcryptokit_stubs.a
%{_libdir}/ocaml/cryptokit/cryptokit*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/cryptokit/cryptokit*.a
%{_libdir}/ocaml/cryptokit/cryptokit*.cmx
%{_libdir}/ocaml/cryptokit/cryptokit*.cmxa
%endif
%{_libdir}/ocaml/cryptokit/dune-package
%{_libdir}/ocaml/cryptokit/opam
%{_examplesdir}/%{name}-%{version}
