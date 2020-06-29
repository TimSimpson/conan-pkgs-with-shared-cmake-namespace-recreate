#include <acme/b.hpp>

#include <acme/a.hpp>

namespace acme::b {
    int Orange::count() {
        ::acme::a::Apple apple;
        return apple.count() / 7;
    }
}
