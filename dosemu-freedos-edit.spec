Summary:	FreeDOS Ripcord edit part
Summary(pl):	Cz�� 'edit' FreeDOSa
Name:		dosemu-freedos-edit
Version:	beta7h01
Release:	4
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/edit1.zip
# Source0-md5:	1875376b1734e5fdb1429c14034894cd
URL:		http://www.freedos.org/
BuildRequires:	unzip
Obsoletes:	dosemu-freedos
Requires:	dosemu
Requires:	dosemu-freedos-minimal
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various text editors for FreeDOS.

%description -l pl
W tym pakiecie mo�na znale�� r�ne edytory tekstu dzia�aj�ce pod
DOS-em.

%prep
%setup -q -c

rm -rf freedos
mkdir freedos
for i in *.ZIP ; do
	unzip -L -o $i -d freedos
done
rm -f freedos/copying

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

cp -Rf freedos $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/dosemu/bootdir/freedos/bin/*
/var/lib/dosemu/bootdir/freedos/doc/*
/var/lib/dosemu/bootdir/freedos/emacs
/var/lib/dosemu/bootdir/freedos/vim
