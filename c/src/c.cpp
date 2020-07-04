#include <acme/c.hpp>
#include <acme/b.hpp>
#include <acme/a.hpp>

namespace acme::c {
    int Banana::count() {
        ::acme::a::Apple apple;
        ::acme::b::Orange orange;
        return orange.count() * apple.count();
    }
}
