Summary:	Cryptographic toolkit for OCaml
Summary(pl):	Biblioteka kryptograficzna dla OCamla
Name:		ocaml-cryptokit
Version:	1.0
Release:	2
License:	LGPL w/ linking exceptions
Group:		Libraries
Vendor:		Xavier Leroy <Xavier.Leroy@inria.fr>
URL:		http://pauillac.inria.fr/~xleroy/software.html
Source0:	http://caml.inria.fr/distrib/bazar-ocaml/cryptokit-%{version}.tar.gz
# Source0-md5:	027a9a5ae4e4b46a4b0934ec683e418c
BuildRequires:	zlib-devel
BuildRequires:	ocaml >= 3.04-7
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

%description -l pl
Biblioteka Cryptokit dostarcza szerok± gamê funkcji kryptograficznych,
które mog± byæ u¿yte w implementacji protoko³ów kryptograficznych w
aplikacjach, dla których wa¿ne jest bezpieczeñstwo. Dostarczane
funkcje to: szyfry symetryczne: AES, DES, 3DES, ARCFour w trybach ECB,
CBC, CFB oraz OFB; szyfr z kluczem publicznym RSA; kryptograficzne
funkcje skrótu i MACi: SHA-1, MD5 oraz MACi bazowane na AES oraz DES;
generacje liczb losowych; kodowania i kompresja: base 64,
szesntastkowa oraz zlib.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych tej biblioteki.

%package devel
Summary:	Cryptographic toolkit for OCaml - development part
Summary(pl):	Biblioteka kryptograficzna dla OCamla - cze¶æ programistyczna
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

%description devel -l pl
Biblioteka Cryptokit dostarcza szerok± gamê funkcji kryptograficznych,
które mog± byæ u¿yte w implementacji protoko³ów kryptograficznych w
aplikacjach, dla których wa¿ne jest bezpieczeñstwo. Dostarczane
funkcje to: szyfry symetryczne: AES, DES, 3DES, ARCFour w trybach ECB,
CBC, CFB oraz OFB; szyfr z kluczem publicznym RSA; kryptograficzne
funkcje skrótu i MACi: SHA-1, MD5 oraz MACi bazowane na AES oraz DES;
generacje liczb losowych; kodowania i kompresja: base 64,
szesntastkowa oraz zlib.

Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
tej biblioteki.

%prep
%setup -q -n cryptokit-%{version}

%build
%{__make} CFLAGS="%{rpmcflags} -fPIC" all allopt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit
%{__make} install INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit
install *.cm[ixa]* *.a dll*.so $RPM_BUILD_ROOT%{_libdir}/ocaml/cryptokit
(cd $RPM_BUILD_ROOT%{_libdir}/ocaml && ln -s cryptokit/dll*.so .)

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r *test.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cryptokit
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cryptokit/META <<EOF
requires = "unix num"
version = "%{version}"
directory = "+cryptokit"
archive(byte) = "cryptokit.cma"
archive(native) = "cryptokit.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/cryptokit
%attr(755,root,root) %{_libdir}/ocaml/cryptokit/*.so
%{_libdir}/ocaml/*.so

%files devel
%defattr(644,root,root,755)
%doc LICENSE README doc
%{_libdir}/ocaml/cryptokit/*.cm[ixa]*
%{_libdir}/ocaml/cryptokit/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/cryptokit
