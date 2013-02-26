Name:           xz-utils
Version:        1
Release:        1%{?dist}
Summary:        Fulfills the requirements of the Steam Linux Client
License:        BSD
Group:          Development/Tools
Source0:        xz-utils.tar
Requires:	xz

%description
Something to make Steam believe all the necessary packages are installed

%prep
%setup -q

%build
%install
%files
%doc

%changelog
* Tue Feb 26 2013 Tim Bielawa <tim@redhat.com> - 1-1
- First and only
