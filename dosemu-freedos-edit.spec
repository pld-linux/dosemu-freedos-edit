Summary:	FreeDOS Ripcord edit part
Summary(pl):	Czê¶æ 'edit' FreeDosa
Name:		dosemu-freedos-edit
Version:	beta7h01
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/edit1.zip
URL:		http://www.freedos.org/
BuildRequires:	unzip
Obsoletes:	dosemu-freedos
Requires:	dosemu
Requires:	dosemu-freedos-minimal
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various text editors for FreeDOS.

%description -l pl
W tym pakiecie mo¿na znale¼æ ró¿ne edytory tekstu dzia³aj±ce pod
DOSem.

%prep
%setup -c %{name} -q

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
