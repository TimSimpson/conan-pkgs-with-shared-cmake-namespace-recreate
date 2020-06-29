#include <acme/a.hpp>
#include <acme/b.hpp>

int main(int argc, const char * * argv) {
    acme::b::Orange orange;
    return 6 == orange.count() ? 0 : 1;
}
