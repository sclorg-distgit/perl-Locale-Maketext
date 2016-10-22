%{?scl:%scl_package perl-Locale-Maketext}

Name:           %{?scl_prefix}perl-Locale-Maketext
Version:        1.27
Release:        2%{?dist}
Summary:        Framework for localization
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Maketext/
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Locale-Maketext-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(I18N::LangTags) >= 0.31
BuildRequires:  %{?scl_prefix}perl(I18N::LangTags::Detect)
BuildRequires:  %{?scl_prefix}perl(integer)
# utf8 is used only if it has already been loaded
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(utf8)
# Optional tests:
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.14
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(I18N::LangTags) >= 0.31
# utf8 is used only if it has already been loaded
Requires:       %{?scl_prefix}perl(warnings)

# Filter under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(I18N::LangTags)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(I18N::LangTags\\)$
%endif

%description
It is a common feature of applications (whether run directly, or via the Web)
for them to be "localized" -- i.e., for them to present an English interface
to an English-speaker, a German interface to a German-speaker, and so on for
all languages it's programmed with. Locale::Maketext is a framework for
software localization; it provides you with the tools for organizing and
accessing the bits of text and text-processing code that you need for
producing localized applications.

%prep
%setup -q -n Locale-Maketext-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.27-2
- SCL

* Thu Jun 23 2016 Petr Pisar <ppisar@redhat.com> - 1.27-1
- 1.27 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-3
- Perl 5.22 rebuild

* Fri Jan 09 2015 Petr Pisar <ppisar@redhat.com> - 1.26-2
- Require undetected warnings module explicitly

* Fri Dec 05 2014 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Mon Nov 11 2013 Petr Pisar <ppisar@redhat.com> - 1.23-293
- Fix escaping backslashes (bug #1026763)

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-292
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.23-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.23-2
- Perl 5.18 rebuild

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> 1.23-1
- Specfile autogenerated by cpanspec 1.78.
