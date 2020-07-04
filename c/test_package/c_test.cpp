#include <acme/a.hpp>
#include <acme/b.hpp>
#include <acme/c.hpp>

int main(int argc, const char * * argv) {
    acme::c::Banana banana;
    return 252 == banana.count() ? 0 : 1;
}
