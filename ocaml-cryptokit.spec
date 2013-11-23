%define		ocaml_ver	1:3.09.2
Summary:	Cryptographic toolkit for OCaml
Summary(pl.UTF-8):	Biblioteka kryptograficzna dla OCamla
Name:		ocaml-cryptokit
Version:	1.9
Release:	1
License:	LGPL w/ linking exceptions
Group:		Libraries
Source0:	http://forge.ocamlcore.org/frs/download.php/1229/cryptokit-%{version}.tar.gz
# Source0-md5:	4432a426c9d260822f4ff2b0750413de
URL:		http://pauillac.inria.fr/~xleroy/software.html
BuildRequires:	ocaml >= %{ocaml_ver}
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
%requires_eq	ocaml

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
%setup -q -n cryptokit-%{version}

%build
./configure \
	--exec-prefix %{_prefix} \
	--prefix %{_prefix} \
	--enable-bench

%{__make} all \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit

install _build/src/{*.cm[ixa]*,*.a,dll*.so} $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit
(cd $RPM_BUILD_ROOT%{_libdir}/ocaml && ln -s cryptokit/dll*.so .)

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r test/*.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cryptokit
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cryptokit/META <<EOF
description = "Cryptographic primitives"
requires = "unix num"
version = "%{version}"
directory = "+cryptokit"
archive(byte) = "cryptokit.cma"
archive(native) = "cryptokit.cmxa"
exists_if = "cryptokit.cma"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt Changes LICENSE.txt README.txt
%dir %{_libdir}/ocaml/cryptokit
%attr(755,root,root) %{_libdir}/ocaml/cryptokit/*.so
%{_libdir}/ocaml/*.so

%files devel
%defattr(644,root,root,755)
%doc _build/src/api-cryptokit.docdir/*
%{_libdir}/ocaml/cryptokit/*.cm[ixa]*
%{_libdir}/ocaml/cryptokit/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/cryptokit
