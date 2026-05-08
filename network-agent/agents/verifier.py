from tools.clash_controller import ClashController

class VerifierAgent:

    def verify(self, proxy_name):

        clash = ClashController()

        delay = clash.test_delay(proxy_name)

        if "delay" in delay:
            if delay["delay"] < 500:
                return True

        return False
