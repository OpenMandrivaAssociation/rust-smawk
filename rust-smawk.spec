%bcond_without check
%global debug_package %{nil}

%global crate smawk

Name:           rust-%{crate}
Version:        0.3.1
Release:        2
Summary:        Functions for finding row-minima in a totally monotone matrix

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/smawk
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
%if %{with check}
BuildRequires:  (crate(num-traits/default) >= 0.2.0 with crate(num-traits/default) < 0.3.0)
BuildRequires:  (crate(rand/default) >= 0.8.0 with crate(rand/default) < 0.9.0)
BuildRequires:  (crate(rand_chacha/default) >= 0.3.0 with crate(rand_chacha/default) < 0.4.0)
BuildRequires:  (crate(version-sync/default) >= 0.9.0 with crate(version-sync/default) < 0.10.0)
%endif
%endif

%global _description %{expand:
Functions for finding row-minima in a totally monotone matrix.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(smawk) = 0.3.1
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(smawk/default) = 0.3.1
Requires:       cargo
Requires:       crate(smawk) = 0.3.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ndarray-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(smawk/ndarray) = 0.3.1
Requires:       cargo
Requires:       (crate(ndarray/default) >= 0.14.0 with crate(ndarray/default) < 0.15.0)
Requires:       crate(smawk) = 0.3.1

%description -n %{name}+ndarray-devel %{_description}

This package contains library source intended for building other packages
which use "ndarray" feature of "%{crate}" crate.

%files       -n %{name}+ndarray-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
