# This is part of the Python test suite.
# The object is registered when you first run the test suite.
# (and hopefully unregistered once done ;-)

# Ensure the vtables in the tlb are known.
from win32com import universal
from win32com.server.exception import COMException
from win32com.client import gencache
import winerror
from win32com.client import constants

#gencache.EnsureModule("{6BCDCB60-5605-11D0-AE5F-CADD4C000000}", 0, 1, 1)
universal.RegisterInterfaces('{6BCDCB60-5605-11D0-AE5F-CADD4C000000}', 0, 1, 1, ["IPyCOMTest"])
 
class PyCOMTest:
	_com_interfaces_ = ['IPyCOMTest']
	_public_methods_ = []
	_reg_clsid_ = "{e743d9cd-cb03-4b04-b516-11d3a81c1597}"
	_reg_progid_ = "Python.Test.PyCOMTest"

	def DoubleString(self, str):
		return str*2
	def DoubleInOutString(self, str):
		return str*2

	def Fire(self, nID):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetLastVarArgs(self):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetMultipleInterfaces(self, outinterface1, outinterface2):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetSafeArrays(self, attrs, attrs2, ints):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetSetDispatch(self, indisp):
		raise COMException(hresult=winerror.E_NOTIMPL)

	# Result is of type IPyCOMTest
	def GetSetInterface(self, ininterface):
		raise COMException(hresult=winerror.E_NOTIMPL)

	# Result is of type IPyCOMTest
	def GetSetInterfaceArray(self, ininterface):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetSetUnknown(self, inunk):
		raise COMException(hresult=winerror.E_NOTIMPL)

	# Result is of type ISimpleCounter
	def GetSimpleCounter(self):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetSimpleSafeArray(self, ints):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def GetStruct(self):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def SetIntSafeArray(self, ints):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def SetVarArgs(self, *args):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def SetVariantSafeArray(self, vars):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def Start(self):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def Stop(self, nID):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def StopAll(self):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def TakeByRefDispatch(self, inout):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def TakeByRefTypedDispatch(self, inout):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def Test(self, key, inval):
		return not inval

	def Test2(self, inval):
		return inval

	def Test3(self, inval):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def Test4(self, inval):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def Test5(self, inout):
		if inout == constants.TestAttr1:
			return constants.TestAttr1_1
		elif inout == constants.TestAttr1_1:
			return constants.TestAttr1
		else:
			return -1

	def TestOptionals(self, strArg='def', sval=0, lval=1, dval=3.1400001049041748):
		raise COMException(hresult=winerror.E_NOTIMPL)

	def TestOptionals2(self, dval, strval='', sval=1):
		raise COMException(hresult=winerror.E_NOTIMPL)

if __name__ == '__main__':
	import win32com.server.register
	win32com.server.register.UseCommandLine(PyCOMTest)
