#!/usr/bin/env bash
set -euo pipefail

if [ -z "$FORMULA_VERSION_NO_V" ]; then
  echo "missing FORUMLA_VERSION_NO_V"
  exit 1
fi
if [ -z "$FORMULA_TGZ_SHA256" ]; then
  echo "missing FORMULA_TGZ_SHA256"
  exit 1
fi

cat << EOF
# typed: true
# frozen_string_literal: true

# This file was automatically generated. DO NOT EDIT.
class Listening < Formula
  desc "List processes listening for network connections"
  homepage "https://github.com/cdzombak/listening"
  url "https://github.com/cdzombak/listening/releases/download/v${FORMULA_VERSION_NO_V}/listening-${FORMULA_VERSION_NO_V}-all.tar.gz"
  sha256 "${FORMULA_TGZ_SHA256}"
  license "LGPL-3.0"

  def install
    bin.install "listening"
  end

  test do
    assert_match("${FORMULA_VERSION_NO_V}", shell_output("#{bin}/listening --version"))
  end
end
EOF
