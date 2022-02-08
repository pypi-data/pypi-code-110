from lauterbach.trace32.rcl._rc._address import Address
from ._error import BaseError


class FunctionError(BaseError):
    pass

class AddressRange(Address):
    # Will be added in a future version of PYRCL.
    pass


def fmt(value: object) -> str:
    if type(value) is bool:
        if value:
            return "TRUE()"
        else:
            return "FALSE()"
    elif type(value) is int:
        # Some TRACE32 functions only accept decimals and no hexadecimals but not the other way around.
        return str(value) + "."
    elif type(value) is float:
        # TRACE32 understands python's stringified floats (found no counter example yet)
        return str(value)
    elif type(value) is str:
        return '"' + value + '"'
    else:
        return str(value)

class FunctionService:
    """Function wrapper for most TRACE32 functions.

    Note: Not all functions are available for all target architectures."""

    def __init__(self, conn):
        self.__conn = conn

    def __call__(self, command: str, unused_rtype = None):
        return self.__conn._fnc(command)

    def access_isguest(self, address: Address) -> bool:
        """TRUE if access class belongs to guest

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2473042>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ACCESS.isGUEST({fmt(address)})", bool)

    def access_isguestex(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"ACCESS.isGUESTEX({fmt(address)})", bool)

    def access_ishypervisor(self, address: Address) -> bool:
        """TRUE if access class belongs to hypervisor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2473495>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ACCESS.isHYPERVISOR({fmt(address)})", bool)

    def access_ishypervisorex(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"ACCESS.isHYPERVISOREX({fmt(address)})", bool)

    def address_access(self, address: Address) -> int:
        """Compare access classes

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1427432>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.ACCESS({fmt(address)})", int)

    def address_access_cmp(self, address1: Address, address2: Address) -> bool:
        """Compare access classes, strict

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2779182>`__.

        Args:
            address1: Positional parameter 1
            address2: Positional parameter 2
        """
        return self(f"ADDRESS.ACCESS.CMP({fmt(address1)}, {fmt(address2)})", bool)

    def address_access_cmpstrict(self, address1: Address, address2: Address) -> bool:
        """Compare access classes, strict

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2780045>`__.

        Args:
            address1: Positional parameter 1
            address2: Positional parameter 2
        """
        return self(f"ADDRESS.ACCESS.CMPSTRICT({fmt(address1)}, {fmt(address2)})", bool)

    def address_expandaccess(self, address: Address) -> Address:
        """Fully qualified access class

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2780036>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.EXPANDACCESS({fmt(address)})", Address)

    def address_expandaccessp(self, address: Address) -> Address:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.EXPANDACCESSP({fmt(address)})", Address)

    def address_instr_len(self, address: Address) -> int:
        """Length of instruction

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1427300>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.INSTR.LEN({fmt(address)})", int)

    def address_isdata(self, address: Address) -> bool:
        """Check if memory class refers to data

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1427502>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isDATA({fmt(address)})", bool)

    def address_isguest(self, address: Address) -> bool:
        """TRUE if address is guest address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2471654>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isGUEST({fmt(address)})", bool)

    def address_isguestex(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isGUESTEX({fmt(address)})", bool)

    def address_ishypervisor(self, address: Address) -> bool:
        """TRUE if address is hypervisor address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2472216>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isHYPERVISOR({fmt(address)})", bool)

    def address_ishypervisorex(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isHYPERVISOREX({fmt(address)})", bool)

    def address_isintermediate(self, address: Address) -> bool:
        """Check if intermediate address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1427220>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isINTERMEDIATE({fmt(address)})", bool)

    def address_isnonsecure(self, address: Address) -> bool:
        """TRUE if non-secure access

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034943>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isNONSECURE({fmt(address)})", bool)

    def address_isnonsecureex(self, address: Address) -> bool:
        """TRUE if non-secure access

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034979>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isNONSECUREEX({fmt(address)})", bool)

    def address_isonchip(self, address: Address) -> bool:
        """TRUE if on-chip address area

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1423895>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isONCHIP({fmt(address)})", bool)

    def address_isphysical(self, address: Address) -> bool:
        """TRUE if physical address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1423807>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isPHYSICAL({fmt(address)})", bool)

    def address_isprogram(self, address: Address) -> bool:
        """TRUE if program address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1423781>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isPROGRAM({fmt(address)})", bool)

    def address_issecure(self, address: Address) -> bool:
        """TRUE if secure access

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2035082>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isSECURE({fmt(address)})", bool)

    def address_issecureex(self, address: Address) -> bool:
        """TRUE if secure access

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2035118>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.isSECUREEX({fmt(address)})", bool)

    def address_machineid(self, address: Address) -> int:
        """Extract machine ID

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2472352>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.MACHINEID({fmt(address)})", int)

    def address_mau(self, address: Address) -> int:
        """Minimal addressable unit size (MAU)

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2264037>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.MAU({fmt(address)})", int)

    def address_offset(self, address: Address) -> int:
        """Address without class

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1423976>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.OFFSET({fmt(address)})", int)

    def address_range_begin(self, addressrange: AddressRange) -> Address:
        """Lowest address value of address range

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1944092>`__.

        Args:
            addressrange: Positional parameter 1
        """
        return self(f"ADDRESS.RANGE.BEGIN({fmt(addressrange)})", Address)

    def address_range_end(self, addressrange: AddressRange) -> Address:
        """Highest address value of address range

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1603511>`__.

        Args:
            addressrange: Positional parameter 1
        """
        return self(f"ADDRESS.RANGE.END({fmt(addressrange)})", Address)

    def address_range_size(self, addressrange: AddressRange) -> int:
        """Size of address range

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2265953>`__.

        Args:
            addressrange: Positional parameter 1
        """
        return self(f"ADDRESS.RANGE.SIZE({fmt(addressrange)})", int)

    def address_segment(self, address: Address) -> int:
        """Segment of an address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1603208>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.SEGMENT({fmt(address)})", int)

    def address_straccess(self, address: Address) -> str:
        """Access class of an address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1423307>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"ADDRESS.STRACCESS({fmt(address)})", str)

    def address_track(self) -> Address:
        return self("ADDRESS.TRACK()", Address)

    def address_track_data(self) -> Address:
        return self("ADDRESS.TRACK.DATA()", Address)

    def address_track_program(self) -> Address:
        return self("ADDRESS.TRACK.PROGram()", Address)

    def aet(self) -> bool:
        """Only available for C5000, C6000, C7000_64.
        """
        return self("AET()", bool)

    def analyzer(self) -> bool:
        """Check if Analyzer command group is available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1413614>`__.
        """
        return self("Analyzer()", bool)

    def analyzer_access_vm(self) -> bool:
        return self("Analyzer.ACCESS.VM()", bool)

    def analyzer_config(self) -> bool:
        """Check if specified PowerTrace connected

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2092571>`__.
        """
        return self("Analyzer.CONFIG()", bool)

    def analyzer_config_ecc8(self) -> bool:
        return self("Analyzer.CONFIG.ECC8()", bool)

    def analyzer_config_fec(self) -> bool:
        return self("Analyzer.CONFIG.FEC()", bool)

    def analyzer_config_ha120(self) -> bool:
        return self("Analyzer.CONFIG.HA120()", bool)

    def analyzer_config_hac(self) -> bool:
        return self("Analyzer.CONFIG.HAC()", bool)

    def analyzer_config_powertrace(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2151159>`__.
        """
        return self("Analyzer.CONFIG.POWERTRACE()", bool)

    def analyzer_config_powertrace2(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2151161>`__.
        """
        return self("Analyzer.CONFIG.POWERTRACE2()", bool)

    def analyzer_config_powertrace2lite(self) -> bool:
        return self("Analyzer.CONFIG.POWERTRACE2LITE()", bool)

    def analyzer_config_powertrace3(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2969130>`__.
        """
        return self("Analyzer.CONFIG.POWERTRACE3()", bool)

    def analyzer_config_powertraceserial(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2151163>`__.
        """
        return self("Analyzer.CONFIG.POWERTRACESERIAL()", bool)

    def analyzer_config_risctrace(self) -> bool:
        """Check if RISC trace module connected

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1440695>`__.
        """
        return self("Analyzer.CONFIG.RISCTRACE()", bool)

    def analyzer_config_sa120(self) -> bool:
        return self("Analyzer.CONFIG.SA120()", bool)

    def analyzer_config_stu(self) -> bool:
        return self("Analyzer.CONFIG.STU()", bool)

    def analyzer_config_tsu(self) -> bool:
        return self("Analyzer.CONFIG.TSU()", bool)

    def analyzer_counter_event(self, counter_name: str) -> int:
        """Get value of trigger program event counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1414190>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"Analyzer.COUNTER.EVENT({fmt(counter_name)})", int)

    def analyzer_counter_extern(self, string: str) -> int:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Analyzer.COUNTER.EXTERN({fmt(string)})", int)

    def analyzer_counter_time(self, counter_name: str) -> float:
        """Get value of trigger program time counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1414040>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"Analyzer.COUNTER.TIME({fmt(counter_name)})", float)

    def analyzer_dsel(self) -> str:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1413960>`__.
        """
        return self("Analyzer.DSEL()", str)

    def analyzer_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853204>`__.
        """
        return self("Analyzer.FIRST()", int)

    def analyzer_flag(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Analyzer.FLAG({fmt(string)})", bool)

    def analyzer_flow_errors(self) -> int:
        """Get number of flow errors / hard errors

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1413819>`__.
        """
        return self("Analyzer.FLOW.ERRORS()", int)

    def analyzer_flow_fifofull(self) -> int:
        """Get number of FIFO overflows

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1906551>`__.
        """
        return self("Analyzer.FLOW.FIFOFULL()", int)

    def analyzer_focus_eye(self, channel: str, c_time: float, c_voltage: float, tm: float, am: float, n: float) -> int:
        """Check quality of data eye

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1907023>`__.

        Args:
            channel: Positional parameter 1
            c_time: Positional parameter 2
            c_voltage: Positional parameter 3
            tm: Positional parameter 4
            am: Positional parameter 5
            n: Positional parameter 6
        """
        return self(f"Analyzer.FOCUS.EYE({fmt(channel)}, {fmt(c_time)}, {fmt(c_voltage)}, {fmt(tm)}, {fmt(am)}, {fmt(n)})", int)

    def analyzer_ischannelup(self) -> bool:
        """Check if serial link is established

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2152185>`__.
        """
        return self("Analyzer.ISCHANNELUP()", bool)

    def analyzer_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1415398>`__.
        """
        return self("Analyzer.MAXSIZE()", int)

    def analyzer_mode(self) -> int:
        """Get Analyzer recording mode

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1414935>`__.
        """
        return self("Analyzer.MODE()", int)

    def analyzer_mode_flow(self) -> bool:
        """Check if Analyzer operates as flowtrace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1414832>`__.
        """
        return self("Analyzer.MODE.FLOW()", bool)

    def analyzer_pcie_config(self, register_field: str) -> int:
        """Value of register field from PCIe configuration

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2535566>`__.

        Args:
            register_field: Positional parameter 1
        """
        return self(f"Analyzer.PCIE.CONFIG({fmt(register_field)})", int)

    def analyzer_pcie_isconfigured(self) -> bool:
        """TRUE if prerequisites are fulfilled

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2544411>`__.
        """
        return self("Analyzer.PCIE.ISCONFIGURED()", bool)

    def analyzer_pcie_islinkup(self) -> bool:
        return self("Analyzer.PCIE.ISLINKUP()", bool)

    def analyzer_pcie_register(self, register_offset: int) -> int:
        """Value of 32-bit register from PCIe configuration

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2535522>`__.

        Args:
            register_offset: Positional parameter 1
        """
        return self(f"Analyzer.PCIE.Register({fmt(register_offset)})", int)

    def analyzer_proberevision(self) -> int:
        """Get revision of StarCore NEXUS probe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2536971>`__.

        Only available for SC100.
        """
        return self("Analyzer.PROBEREVISION()", int)

    def analyzer_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1221797>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Analyzer.RECORD.ADDRESS({fmt(record_number)})", Address)

    def analyzer_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1415755>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Analyzer.RECORD.DATA({fmt(record_number)})", int)

    def analyzer_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2161249>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Analyzer.RECORD.OFFSET({fmt(record_number)})", int)

    def analyzer_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1161208>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Analyzer.RECORD.TIME({fmt(record_number)})", float)

    def analyzer_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2163075>`__.
        """
        return self("Analyzer.RECORDS()", int)

    def analyzer_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1416424>`__.
        """
        return self("Analyzer.REF()", int)

    def analyzer_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1416321>`__.
        """
        return self("Analyzer.SIZE()", int)

    def analyzer_state(self) -> int:
        """Get state of Analyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1416015>`__.
        """
        return self("Analyzer.STATE()", int)

    def analyzer_threshold(self) -> float:
        """Get threshold voltage of parallel preprocessor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1415924>`__.
        """
        return self("Analyzer.THRESHOLD()", float)

    def analyzer_traceconnect(self) -> str:
        """Name of trace sink of the SoC

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2171555>`__.
        """
        return self("Analyzer.TraceCONNECT()", str)

    def analyzer_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1165434>`__.
        """
        return self("Analyzer.TRACK.RECORD()", int)

    def analyzer_trigger_a(self) -> int:
        return self("Analyzer.TRIGGER.A()", int)

    def analyzer_trigger_b(self) -> int:
        return self("Analyzer.TRIGGER.B()", int)

    def analyzer_trigger_time(self) -> float:
        """Time of trigger point in trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2178208>`__.
        """
        return self("Analyzer.TRIGGER.TIME()", float)

    def area_count(self) -> int:
        """Number of existing message areas

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1700282>`__.
        """
        return self("AREA.COUNT()", int)

    def area_exist(self, area_name: str) -> bool:
        """Check if message area exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698208>`__.

        Args:
            area_name: Positional parameter 1
        """
        return self(f"AREA.EXIST({fmt(area_name)})", bool)

    def area_line(self, area_name: str, line: int) -> str:
        """Extract line from message area

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698238>`__.

        Args:
            area_name: Positional parameter 1
            line: Positional parameter 2
        """
        return self(f"AREA.LINE({fmt(area_name)}, {fmt(line)})", str)

    def area_maxcount(self) -> int:
        """Maximal number of message areas

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698662>`__.
        """
        return self("AREA.MAXCOUNT()", int)

    def area_name(self, index: int) -> str:
        """Names of existing message areas

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698298>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"AREA.NAME({fmt(index)})", str)

    def area_selected(self) -> str:
        """Name of active message area

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698335>`__.
        """
        return self("AREA.SELECTed()", str)

    def area_size_columns(self, area_name: str) -> int:
        """Columns of a message area

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1700036>`__.

        Args:
            area_name: Positional parameter 1
        """
        return self(f"AREA.SIZE.COLUMNS({fmt(area_name)})", int)

    def area_size_lines(self, area_name: str) -> int:
        """Lines of a message area

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1698558>`__.

        Args:
            area_name: Positional parameter 1
        """
        return self(f"AREA.SIZE.LINES({fmt(area_name)})", int)

    def arm64(self) -> bool:
        """Only available for ARM.
        """
        return self("ARM64()", bool)

    def armarchversion(self, parameter: str) -> int:
        """ARM architecture version of CPU

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1412337>`__.

        Only available for ARM.

        Args:
            parameter: Positional parameter 1
        """
        return self(f"ARMARCHVERSION({fmt(parameter)})", int)

    def art_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853089>`__.
        """
        return self("ART.FIRST()", int)

    def art_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630245>`__.
        """
        return self("ART.MAXSIZE()", int)

    def art_mode(self) -> int:
        """Get ART recording mode

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2096066>`__.
        """
        return self("ART.MODE()", int)

    def art_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630282>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"ART.RECORD.ADDRESS({fmt(record_number)})", Address)

    def art_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630293>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"ART.RECORD.OFFSET({fmt(record_number)})", int)

    def art_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630304>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"ART.RECORD.TIME({fmt(record_number)})", float)

    def art_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630316>`__.
        """
        return self("ART.RECORDS()", int)

    def art_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630328>`__.
        """
        return self("ART.REF()", int)

    def art_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630339>`__.
        """
        return self("ART.SIZE()", int)

    def art_state(self) -> int:
        """Get state of ART trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2214101>`__.
        """
        return self("ART.STATE()", int)

    def art_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1630388>`__.
        """
        return self("ART.TRACK.RECORD()", int)

    def atrace_records(self) -> int:
        return self("ATrace.RECORDS()", int)

    def atrace_ref(self) -> int:
        return self("ATrace.REF()", int)

    def atrace_size(self) -> int:
        return self("ATrace.SIZE()", int)

    def atrace_state(self) -> int:
        return self("ATrace.STATE()", int)

    def autofocus(self) -> bool:
        """TRUE if AutoFocus preprocessor attached

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1419937>`__.
        """
        return self("AUTOFOCUS()", bool)

    def autofocus_frequency(self) -> int:
        """Frequency of trace-port clock

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1419818>`__.
        """
        return self("AUTOFOCUS.FREQUENCY()", int)

    def autofocus_ok(self) -> bool:
        """TRUE if command execution successful

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1419914>`__.
        """
        return self("AUTOFOCUS.OK()", bool)

    def avx(self, register_name_dot_column_number: str) -> int:
        """Content of AVX register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1419276>`__.

        Only available for I386, I386_64.

        Args:
            register_name_dot_column_number: Positional parameter 1
        """
        return self(f"AVX({fmt(register_name_dot_column_number)})", int)

    def avx512(self, register_name_dot_column_number: str) -> int:
        """Content of AVX512 register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2558959>`__.

        Only available for I386, I386_64.

        Args:
            register_name_dot_column_number: Positional parameter 1
        """
        return self(f"AVX512({fmt(register_name_dot_column_number)})", int)

    def bmc_clock(self) -> int:
        """Frequency of core clock

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2020048>`__.
        """
        return self("BMC.CLOCK()", int)

    def bmc_counter(self, counter_index: int) -> int:
        """Value of a benchmark counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1412984>`__.

        Args:
            counter_index: Positional parameter 1
        """
        return self(f"BMC.COUNTER({fmt(counter_index)})", int)

    def bmc_counter_byname(self, counter_name: str) -> int:
        """Value of a benchmark counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2167594>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"BMC.COUNTER.BYNAME({fmt(counter_name)})", int)

    def bmc_counter_byname_core(self, counter_name: str, core_index: int) -> int:
        """Value of a benchmark counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2167879>`__.

        Args:
            counter_name: Positional parameter 1
            core_index: Positional parameter 2
        """
        return self(f"BMC.COUNTER.BYNAME.CORE({fmt(counter_name)}, {fmt(core_index)})", int)

    def bmc_counter_core(self, counter_index: int, core_index: int) -> int:
        """Value of a benchmark counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2167832>`__.

        Args:
            counter_index: Positional parameter 1
            core_index: Positional parameter 2
        """
        return self(f"BMC.COUNTER.CORE({fmt(counter_index)}, {fmt(core_index)})", int)

    def bmc_overflow(self, counter_index: int) -> bool:
        """TRUE if benchmark counter overflow

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2167196>`__.

        Args:
            counter_index: Positional parameter 1
        """
        return self(f"BMC.OVERFLOW({fmt(counter_index)})", bool)

    def bmc_overflow_byname(self, counter_name: str) -> bool:
        """TRUE if benchmark counter overflow

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2168064>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"BMC.OVERFLOW.BYNAME({fmt(counter_name)})", bool)

    def bmc_overflow_byname_core(self, counter_name: str, core_index: int) -> bool:
        """TRUE if benchmark counter overflow

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2168143>`__.

        Args:
            counter_name: Positional parameter 1
            core_index: Positional parameter 2
        """
        return self(f"BMC.OVERFLOW.BYNAME.CORE({fmt(counter_name)}, {fmt(core_index)})", bool)

    def bmc_overflow_core(self, counter_index: int, core_index: int) -> bool:
        """TRUE if benchmark counter overflow

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2167289>`__.

        Args:
            counter_index: Positional parameter 1
            core_index: Positional parameter 2
        """
        return self(f"BMC.OVERFLOW.CORE({fmt(counter_index)}, {fmt(core_index)})", bool)

    def break_alpha_exist(self, address: Address) -> bool:
        """TRUE if Alpha breakpoint exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1977903>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Break.Alpha.EXIST({fmt(address)})", bool)

    def break_beta_exist(self, address: Address) -> bool:
        """TRUE if Beta breakpoint exist

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1978272>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Break.Beta.EXIST({fmt(address)})", bool)

    def break_charly_exist(self, address: Address) -> bool:
        """TRUE if Charly breakpoint exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1978320>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Break.Charly.EXIST({fmt(address)})", bool)

    def break_program_exist(self, address: Address) -> bool:
        """TRUE if enabled program breakpoint exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2256912>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Break.Program.EXIST({fmt(address)})", bool)

    def break_readwrite_exist(self, address: Address) -> bool:
        """TRUE if enabled data address breakpoint exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2256743>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Break.ReadWrite.EXIST({fmt(address)})", bool)

    def bsdl_check_bypass(self) -> bool:
        """Chain bypass test

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1421183>`__.
        """
        return self("BSDL.CHECK.BYPASS()", bool)

    def bsdl_check_flashconf(self) -> bool:
        """Flash configuration test

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1421094>`__.
        """
        return self("BSDL.CHECK.FLASHCONF()", bool)

    def bsdl_check_idcode(self) -> bool:
        """Chain IDCODE test

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1420961>`__.
        """
        return self("BSDL.CHECK.IDCODE()", bool)

    def bsdl_getdrbit(self, chip_number: int, bit_number: int) -> int:
        """Data register bit

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1420855>`__.

        Args:
            chip_number: Positional parameter 1
            bit_number: Positional parameter 2
        """
        return self(f"BSDL.GetDRBit({fmt(chip_number)}, {fmt(bit_number)})", int)

    def bsdl_getportlevel(self, chip_number: int, port_name: str) -> int:
        """Port level value

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1811640>`__.

        Args:
            chip_number: Positional parameter 1
            port_name: Positional parameter 2
        """
        return self(f"BSDL.GetPortLevel({fmt(chip_number)}, {fmt(port_name)})", int)

    def btrace_records(self) -> int:
        return self("BTrace.RECORDS()", int)

    def btrace_ref(self) -> int:
        return self("BTrace.REF()", int)

    def btrace_size(self) -> int:
        return self("BTrace.SIZE()", int)

    def btrace_state(self) -> int:
        return self("BTrace.STATE()", int)

    def cable_galvanicisolation(self) -> bool:
        """Cable has galvanic isolation

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2226225>`__.
        """
        return self("CABLE.GalvanicISOlation()", bool)

    def cable_galvanicisolation_serial(self) -> str:
        """Serial number of adapter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2226041>`__.
        """
        return self("CABLE.GalvanicISOlation.SERIAL()", str)

    def cable_name(self) -> str:
        """Name of debug cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1422125>`__.
        """
        return self("CABLE.NAME()", str)

    def cable_serial(self) -> str:
        """Serial number of debug cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1422024>`__.
        """
        return self("CABLE.SERIAL()", str)

    def cable_twowire(self) -> bool:
        """TRUE if two-wire debugging supported

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1421880>`__.
        """
        return self("CABLE.TWOWIRE()", bool)

    def cache_dc_dirty(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435313>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.DC.DIRTY({fmt(set)}, {fmt(way)})", bool)

    def cache_dc_dirtymask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435624>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.DC.DIRTYMASK({fmt(set)}, {fmt(way)})", int)

    def cache_dc_lru(self, set: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435500>`__.

        Args:
            set: Positional parameter 1
        """
        return self(f"CACHE.DC.LRU({fmt(set)})", int)

    def cache_dc_tag(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435420>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.DC.TAG({fmt(set)}, {fmt(way)})", int)

    def cache_dc_valid(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435344>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.DC.VALID({fmt(set)}, {fmt(way)})", bool)

    def cache_dc_validmask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434995>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.DC.VALIDMASK({fmt(set)}, {fmt(way)})", int)

    def cache_ic_dirty(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435208>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.IC.DIRTY({fmt(set)}, {fmt(way)})", bool)

    def cache_ic_dirtymask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435121>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.IC.DIRTYMASK({fmt(set)}, {fmt(way)})", int)

    def cache_ic_lru(self, set: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435029>`__.

        Args:
            set: Positional parameter 1
        """
        return self(f"CACHE.IC.LRU({fmt(set)})", int)

    def cache_ic_tag(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1433600>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.IC.TAG({fmt(set)}, {fmt(way)})", int)

    def cache_ic_valid(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434883>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.IC.VALID({fmt(set)}, {fmt(way)})", bool)

    def cache_ic_validmask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434816>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.IC.VALIDMASK({fmt(set)}, {fmt(way)})", int)

    def cache_l2_dirty(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434734>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.DIRTY({fmt(set)}, {fmt(way)})", bool)

    def cache_l2_dirtymask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434668>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.DIRTYMASK({fmt(set)}, {fmt(way)})", int)

    def cache_l2_lru(self, set: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1809052>`__.

        Args:
            set: Positional parameter 1
        """
        return self(f"CACHE.L2.LRU({fmt(set)})", int)

    def cache_l2_shared(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434522>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.SHARED({fmt(set)}, {fmt(way)})", bool)

    def cache_l2_sharedmask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434448>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.SHAREDMASK({fmt(set)}, {fmt(way)})", int)

    def cache_l2_tag(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434367>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.TAG({fmt(set)}, {fmt(way)})", int)

    def cache_l2_valid(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434286>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.VALID({fmt(set)}, {fmt(way)})", bool)

    def cache_l2_validmask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434216>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L2.VALIDMASK({fmt(set)}, {fmt(way)})", int)

    def cache_l3_dirty(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434150>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L3.DIRTY({fmt(set)}, {fmt(way)})", bool)

    def cache_l3_dirtymask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1434084>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L3.DIRTYMASK({fmt(set)}, {fmt(way)})", int)

    def cache_l3_lru(self, set: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1433998>`__.

        Args:
            set: Positional parameter 1
        """
        return self(f"CACHE.L3.LRU({fmt(set)})", int)

    def cache_l3_tag(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1433917>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L3.TAG({fmt(set)}, {fmt(way)})", int)

    def cache_l3_valid(self, set: int, way: int) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1433894>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L3.VALID({fmt(set)}, {fmt(way)})", bool)

    def cache_l3_validmask(self, set: int, way: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1433634>`__.

        Args:
            set: Positional parameter 1
            way: Positional parameter 2
        """
        return self(f"CACHE.L3.VALIDMASK({fmt(set)}, {fmt(way)})", int)

    def canalyzer(self) -> bool:
        """Check if CAnalyzer command group is available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541118>`__.
        """
        return self("CAnalyzer()", bool)

    def canalyzer_bothcables(self) -> bool:
        """TRUE if both debug cables are plugged

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1428079>`__.
        """
        return self("CAnalyzer.BOTHCables()", bool)

    def canalyzer_cabletype(self, number: int) -> int:
        """Type of adapter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2754209>`__.

        Args:
            number: Positional parameter 1
        """
        return self(f"CAnalyzer.CableTYPE({fmt(number)})", int)

    def canalyzer_debugcable(self) -> str:
        """CombiProbe whisker cable is A or B

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1804916>`__.
        """
        return self("CAnalyzer.DebugCable()", str)

    def canalyzer_feature(self, feature: str) -> bool:
        """Query features of CAnalyzer hardware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2753969>`__.

        Args:
            feature: Positional parameter 1
        """
        return self(f"CAnalyzer.FEATURE({fmt(feature)})", bool)

    def canalyzer_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2753951>`__.
        """
        return self("CAnalyzer.FIRST()", int)

    def canalyzer_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425990>`__.
        """
        return self("CAnalyzer.MAXSIZE()", int)

    def canalyzer_pin(self, pin_name: str) -> int:
        """Status of trace pins

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425894>`__.

        Args:
            pin_name: Positional parameter 1
        """
        return self(f"CAnalyzer.PIN({fmt(pin_name)})", int)

    def canalyzer_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425771>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"CAnalyzer.RECORD.ADDRESS({fmt(record_number)})", Address)

    def canalyzer_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425674>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"CAnalyzer.RECORD.DATA({fmt(record_number)})", int)

    def canalyzer_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425578>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"CAnalyzer.RECORD.OFFSET({fmt(record_number)})", int)

    def canalyzer_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425480>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"CAnalyzer.RECORD.TIME({fmt(record_number)})", float)

    def canalyzer_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425376>`__.
        """
        return self("CAnalyzer.RECORDS()", int)

    def canalyzer_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1425296>`__.
        """
        return self("CAnalyzer.REF()", int)

    def canalyzer_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2201197>`__.
        """
        return self("CAnalyzer.SIZE()", int)

    def canalyzer_state(self) -> int:
        """Get state of Compact Analyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2200727>`__.
        """
        return self("CAnalyzer.STATE()", int)

    def canalyzer_traceconnect(self) -> str:
        """Name of trace sink of the SoC

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2515420>`__.
        """
        return self("CAnalyzer.TraceCONNECT()", str)

    def canalyzer_traceport(self) -> str:
        """CombiProbe whisker cable is A or B

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1424906>`__.
        """
        return self("CAnalyzer.TracePort()", str)

    def canalyzer_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1424785>`__.
        """
        return self("CAnalyzer.TRACK.RECORD()", int)

    def cerberus_ioinfo(self) -> int:
        """IOINFO of Cerberus module

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1578311>`__.

        Only available for TRICORE.
        """
        return self("CERBERUS.IOINFO()", int)

    def cerberus_ioinfo_iflck(self) -> bool:
        """TRUE if IF_LCK bit in Cerberus INONFO set

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1577963>`__.

        Only available for TRICORE.
        """
        return self("CERBERUS.IOINFO.IFLCK()", bool)

    def chip_emulationdevice(self) -> bool:
        """TRUE if emulation device

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543428>`__.

        Only available for ARM, C166, ETPU, GTM, PCP, POWERPC, POWERPC64, TRICORE.
        """
        return self("CHIP.EmulationDevice()", bool)

    def chip_gtm_atommodule(self) -> int:
        """Only available for GTM, V800.
        """
        return self("CHIP.GTM.ATOMModule()", int)

    def chip_gtm_mcsmodule(self) -> int:
        """Only available for GTM, V800.
        """
        return self("CHIP.GTM.MCSModule()", int)

    def chip_gtm_timmodule(self) -> int:
        """Only available for GTM, V800.
        """
        return self("CHIP.GTM.TIMModule()", int)

    def chip_gtm_tiomodule(self) -> int:
        """Only available for GTM, V800.
        """
        return self("CHIP.GTM.TIOModule()", int)

    def chip_gtm_tommodule(self) -> int:
        """Only available for GTM, V800.
        """
        return self("CHIP.GTM.TOMModule()", int)

    def chip_gtmversion(self) -> int:
        """Only available for GTM.
        """
        return self("CHIP.GTMVersion()", int)

    def chip_securechallenge(self, number: int) -> int:
        """Only available for ARM, POWERPC, POWERPC64.

        Args:
            number: Positional parameter 1
        """
        return self(f"CHIP.SecureChallenge({fmt(number)})", int)

    def chip_securestatus(self, string: str) -> int:
        """Only available for POWERPC, POWERPC64.

        Args:
            string: Positional parameter 1
        """
        return self(f"CHIP.SecureStatus({fmt(string)})", int)

    def chip_stepping(self) -> str:
        """Major silicon step of an TriCore AURIX device

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543440>`__.

        Only available for GTM, TRICORE.
        """
        return self("CHIP.STEPping()", str)

    def ciprobe(self) -> bool:
        """TRUE if Compact Analyzer hardware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543491>`__.
        """
        return self("CIProbe()", bool)

    def ciprobe_adc_enable(self, channel: str) -> bool:
        """TRUE if channel is enabled

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543501>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"CIProbe.ADC.ENABLE({fmt(channel)})", bool)

    def ciprobe_adc_shunt(self, channel: str) -> float:
        """Get shunt-resistor value

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543511>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"CIProbe.ADC.SHUNT({fmt(channel)})", float)

    def ciprobe_analog(self) -> bool:
        return self("CIProbe.ANALOG()", bool)

    def ciprobe_digital(self) -> bool:
        return self("CIProbe.DIGITAL()", bool)

    def ciprobe_first(self) -> int:
        return self("CIProbe.FIRST()", int)

    def ciprobe_get(self, string: str) -> int:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"CIProbe.GET({fmt(string)})", int)

    def ciprobe_getanalog(self, string: str) -> float:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"CIProbe.GETAnalog({fmt(string)})", float)

    def ciprobe_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543521>`__.
        """
        return self("CIProbe.MAXSIZE()", int)

    def ciprobe_record_data(self, number: int, string: str) -> int:
        """
        Args:
            number: Positional parameter 1
            string: Positional parameter 2
        """
        return self(f"CIProbe.RECORD.DATA({fmt(number)}, {fmt(string)})", int)

    def ciprobe_record_time(self, number: int) -> float:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"CIProbe.RECORD.TIME({fmt(number)})", float)

    def ciprobe_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543532>`__.
        """
        return self("CIProbe.RECORDS()", int)

    def ciprobe_ref(self) -> int:
        return self("CIProbe.REF()", int)

    def ciprobe_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543542>`__.
        """
        return self("CIProbe.SIZE()", int)

    def ciprobe_state(self) -> int:
        """Get state of Compact Analyzer for CIProbe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543553>`__.
        """
        return self("CIProbe.STATE()", int)

    def ciprobe_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543588>`__.
        """
        return self("CIProbe.TRACK.RECORD()", int)

    def cmibase(self, instance: int) -> Address:
        """Base addresses of CMI modules

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2711261>`__.

        Only available for ARM, C6000, C7000_64.

        Args:
            instance: Positional parameter 1
        """
        return self(f"CMIBASE({fmt(instance)})", Address)

    def cmn_periphbase(self, number: int) -> Address:
        """Only available for ARM.

        Args:
            number: Positional parameter 1
        """
        return self(f"CMN.PERIPHBASE({fmt(number)})", Address)

    def cmn_rootnodebase(self, number: int) -> Address:
        """Only available for ARM.

        Args:
            number: Positional parameter 1
        """
        return self(f"CMN.ROOTNODEBASE({fmt(number)})", Address)

    def cmnbase(self, number: int) -> Address:
        """Only available for ARM.

        Args:
            number: Positional parameter 1
        """
        return self(f"CMNBASE({fmt(number)})", Address)

    def component_available(self, component_name: str) -> bool:
        """TRUE if peripheral component available on CPU

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1428577>`__.

        Args:
            component_name: Positional parameter 1
        """
        return self(f"COMPonent.AVAILABLE({fmt(component_name)})", bool)

    def component_base(self, component_name: str, core: int) -> Address:
        """Base address of peripheral component

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1428445>`__.

        Args:
            component_name: Positional parameter 1
            core: Positional parameter 2
        """
        return self(f"COMPonent.BASE({fmt(component_name)}, {fmt(core)})", Address)

    def component_name(self, component_name: str, core: int) -> str:
        """Name of peripheral component

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2497332>`__.

        Args:
            component_name: Positional parameter 1
            core: Positional parameter 2
        """
        return self(f"COMPonent.NAME({fmt(component_name)}, {fmt(core)})", str)

    def component_property_address(self, string1: str, string2: str, number: int) -> Address:
        """
        Args:
            string1: Positional parameter 1
            string2: Positional parameter 2
            number: Positional parameter 3
        """
        return self(f"COMPonent.PROPerty.ADDRess({fmt(string1)}, {fmt(string2)}, {fmt(number)})", Address)

    def component_type(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"COMPonent.TYPE({fmt(string)})", str)

    def config_screen(self) -> bool:
        """Check if screen output is switched on

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342499>`__.
        """
        return self("CONFIG.SCREEN()", bool)

    def confignumber(self) -> int:
        """Number of cores configured in TRACE32

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1147750>`__.
        """
        return self("CONFIGNUMBER()", int)

    def convert_addresstodualport(self, address: Address) -> Address:
        """Dualport access class

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853971>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"CONVert.ADDRESSTODUALPORT({fmt(address)})", Address)

    def convert_addresstononsecure(self, address: Address) -> Address:
        """Non-secure access class

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853869>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"CONVert.ADDRESSTONONSECURE({fmt(address)})", Address)

    def convert_addresstosecure(self, address: Address) -> Address:
        """Secure access class

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853780>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"CONVert.ADDRESSTOSECURE({fmt(address)})", Address)

    def convert_booltoint(self, flag: bool) -> int:
        """See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573254>`__.

        Args:
            flag: Positional parameter 1
        """
        return self(f"CONVert.BOOLTOINT({fmt(flag)})", int)

    def convert_floattoint(self, float_number: float) -> int:
        """Float to integer

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1371419>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"CONVert.FLOATTOINT({fmt(float_number)})", int)

    def convert_hextoint(self, hex: int) -> int:
        """Hex to integer

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1371131>`__.

        Args:
            hex: Positional parameter 1
        """
        return self(f"CONVert.HEXTOINT({fmt(hex)})", int)

    def convert_inttoaddress(self, number1: int, number2: int) -> Address:
        """
        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
        """
        return self(f"CONVert.INTTOADDRESS({fmt(number1)}, {fmt(number2)})", Address)

    def convert_inttobool(self, integer: int) -> bool:
        """Integer to boolean

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1371003>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"CONVert.INTTOBOOL({fmt(integer)})", bool)

    def convert_inttofloat(self, integer: int) -> float:
        """Integer to floating point value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1370841>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"CONVert.INTTOFLOAT({fmt(integer)})", float)

    def convert_inttohex(self, integer: int) -> int:
        """Integer to hex

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1370721>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"CONVert.INTTOHEX({fmt(integer)})", int)

    def convert_linear11tofloat(self, number: int) -> float:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"CONVert.LINEAR11TOFLOAT({fmt(number)})", float)

    def convert_linear16tofloat(self, number1: int, number2: int) -> float:
        """
        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
        """
        return self(f"CONVert.LINEAR16TOFLOAT({fmt(number1)}, {fmt(number2)})", float)

    def convert_octaltoint(self, string: str) -> int:
        """Octal to decimal

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1370158>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"CONVert.OCTaltoint({fmt(string)})", int)

    def convert_signedbyte(self, value: int) -> int:
        """1 byte to 8 bytes

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1370129>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"CONVert.SignedByte({fmt(value)})", int)

    def convert_signedlong(self, value: int) -> int:
        """4 bytes to 8 bytes

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1392995>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"CONVert.SignedLong({fmt(value)})", int)

    def convert_signedword(self, value: int) -> int:
        """2 bytes to 8 bytes

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1619013>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"CONVert.SignedWord({fmt(value)})", int)

    def convert_tolower(self, string: str) -> str:
        """String to lower case

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1368016>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"CONVert.TOLOWER({fmt(string)})", str)

    def convert_toupper(self, string: str) -> str:
        """String to upper case

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1367787>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"CONVert.TOUPPER({fmt(string)})", str)

    def core(self) -> int:
        """Get the selected core

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1437054>`__.
        """
        return self("CORE()", int)

    def core_isactive(self, core: str) -> bool:
        """TRUE if this core is active

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2020794>`__.

        Args:
            core: Positional parameter 1
        """
        return self(f"CORE.ISACTIVE({fmt(core)})", bool)

    def core_isassigned(self, core_number: int) -> bool:
        """TRUE if physical core is assigned to debug session

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1549315>`__.

        Args:
            core_number: Positional parameter 1
        """
        return self(f"CORE.ISASSIGNED({fmt(core_number)})", bool)

    def core_logicaltophysical(self, core_number: int) -> int:
        """This is the physical core number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1549554>`__.

        Args:
            core_number: Positional parameter 1
        """
        return self(f"CORE.LOGICALTOPHYSICAL({fmt(core_number)})", int)

    def core_names(self, index: int) -> str:
        """Physical core names assigned to TRACE32

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2021627>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"CORE.NAMES({fmt(index)})", str)

    def core_number(self) -> int:
        """Number of logical cores

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1549715>`__.
        """
        return self("CORE.NUMBER()", int)

    def core_physicaltological(self, core_number: int) -> int:
        """Logical core number of physical core

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1550169>`__.

        Args:
            core_number: Positional parameter 1
        """
        return self(f"CORE.PHYSICALTOLOGICAL({fmt(core_number)})", int)

    def corebase(self) -> Address:
        """Only available for ARM.
        """
        return self("COREBASE()", Address)

    def corename(self) -> str:
        """Name of core within selected chip

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1436872>`__.
        """
        return self("CORENAME()", str)

    def coretype(self) -> int:
        """Only available for ARC.
        """
        return self("CORETYPE()", int)

    def count_frequency(self) -> int:
        """Frequency of last measurement

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1631195>`__.
        """
        return self("Count.Frequency()", int)

    def count_level(self) -> int:
        """Level of frequency counter input

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1437584>`__.
        """
        return self("Count.LEVEL()", int)

    def count_time(self) -> float:
        """Time of last measurement

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1631925>`__.
        """
        return self("Count.Time()", float)

    def count_value(self) -> int:
        """Samples of the Count.GO command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1437515>`__.
        """
        return self("Count.VALUE()", int)

    def coverage_bdone(self, address_range: AddressRange) -> int:
        """Byte count of all executed instructions

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2257071>`__.

        Args:
            address_range: Positional parameter 1
        """
        return self(f"COVerage.BDONE({fmt(address_range)})", int)

    def coverage_isconditiontrue(self) -> bool:
        return self("COVerage.IsConditionTrue()", bool)

    def coverage_load_key(self) -> str:
        return self("COVerage.LOAD.KEY()", str)

    def coverage_scope(self, address_range: AddressRange) -> int:
        """Degree of code coverage

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543713>`__.

        Args:
            address_range: Positional parameter 1
        """
        return self(f"COVerage.SCOPE({fmt(address_range)})", int)

    def coverage_sourcemetric(self) -> str:
        """Active code coverage criterion

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2518349>`__.
        """
        return self("COVerage.SourceMetric()", str)

    def coverage_treewalk(self, action: str) -> str:
        """Walk symbol tree

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1815258>`__.

        Args:
            action: Positional parameter 1
        """
        return self(f"COVerage.TreeWalk({fmt(action)})", str)

    def cp15(self, number: int) -> int:
        """Only available for ARM.

        Args:
            number: Positional parameter 1
        """
        return self(f"CP15({fmt(number)})", int)

    def cpu(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1490200>`__.
        """
        return self("CPU()", str)

    def cpu_address(self, section: str) -> Address:
        """Section start address of given core

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2673254>`__.

        Only available for ARC, TRICORE.

        Args:
            section: Positional parameter 1
        """
        return self(f"CPU.ADDRESS({fmt(section)})", Address)

    def cpu_address_physicalindex(self, section: int, core_number: str) -> Address:
        """Section start address of given core

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2814114>`__.

        Only available for TRICORE.

        Args:
            section: Positional parameter 1
            core_number: Positional parameter 2
        """
        return self(f"CPU.ADDRESS.PhysicalINDEX({fmt(section)}, {fmt(core_number)})", Address)

    def cpu_basefamily(self) -> str:
        """Only available for V800.
        """
        return self("CPU.BASEFAMILY()", str)

    def cpu_deviceid(self) -> int:
        """Only available for V800.
        """
        return self("CPU.DEVICEID()", int)

    def cpu_feature(self, feature_string: str) -> bool:
        """TRUE if CPU feature exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2809357>`__.

        Args:
            feature_string: Positional parameter 1
        """
        return self(f"CPU.FEATURE({fmt(feature_string)})", bool)

    def cpu_pincount(self) -> str:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2022615>`__.

        Only available for V800.
        """
        return self("CPU.PINCOUNT()", str)

    def cpu_subfamily(self) -> str:
        """Only available for V800.
        """
        return self("CPU.SUBFAMILY()", str)

    def cpubondout(self) -> str:
        """Name of boundout processor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1438214>`__.
        """
        return self("CPUBONDOUT()", str)

    def cpucoreversion(self) -> str:
        """Core or architecture version of CPU

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1438152>`__.
        """
        return self("CPUCOREVERSION()", str)

    def cpufamily(self) -> str:
        """Family name of processor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1438018>`__.
        """
        return self("CPUFAMILY()", str)

    def cpuflashtype(self) -> str:
        """Only available for V800.
        """
        return self("CPUFLASHTYPE()", str)

    def cpuis(self, search_string: str) -> bool:
        """TRUE if 64-bit architecture

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1437848>`__.

        Args:
            search_string: Positional parameter 1
        """
        return self(f"CPUIS({fmt(search_string)})", bool)

    def cpuis64bit(self) -> bool:
        """TRUE if 64-bit architecture

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1437657>`__.
        """
        return self("CPUIS64BIT()", bool)

    def ctibase(self) -> Address:
        """Only available for ARM.
        """
        return self("CTIBASE()", Address)

    def dap_available(self) -> bool:
        """TRUE if debugging via DAP is supported

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1442543>`__.

        Only available for C166, GTM, I51, PCP, TRICORE.
        """
        return self("DAP.Available()", bool)

    def dap_user0(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1442210>`__.

        Only available for C166, GTM, I51, PCP, TRICORE.
        """
        return self("DAP.USER0()", bool)

    def dap_user1(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1442192>`__.

        Only available for C166, GTM, I51, PCP, TRICORE.
        """
        return self("DAP.USER1()", bool)

    def data_al_errors(self) -> int:
        """Get number of errors detected by Data.AllocList

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1447225>`__.
        """
        return self("Data.AL.ERRORS()", int)

    def data_byte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287946>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Byte({fmt(address)})", int)

    def data_float(self, format: str, address: Address) -> float:
        """Get floating point number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1446808>`__.

        Args:
            format: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"Data.Float({fmt(format)}, {fmt(address)})", float)

    def data_hbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287958>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.HByte({fmt(address)})", int)

    def data_jumptarget(self, address: Address) -> int:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"Data.JUMPTARGET({fmt(address)})", int)

    def data_long(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287954>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long({fmt(address)})", int)

    def data_long_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283437>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long.BigEndian({fmt(address)})", int)

    def data_long_byte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291867>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long.Byte({fmt(address)})", int)

    def data_long_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283439>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long.LittleEndian({fmt(address)})", int)

    def data_long_long(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291870>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long.Long({fmt(address)})", int)

    def data_long_word(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291869>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Long.Word({fmt(address)})", int)

    def data_longlong(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287966>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.LongLong({fmt(address)})", int)

    def data_longlong_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283441>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.LongLong.BigEndian({fmt(address)})", int)

    def data_longlong_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283443>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.LongLong.LittleEndian({fmt(address)})", int)

    def data_pbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287956>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.PByte({fmt(address)})", int)

    def data_quad(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287964>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad({fmt(address)})", int)

    def data_quad_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283445>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.BigEndian({fmt(address)})", int)

    def data_quad_byte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291872>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.Byte({fmt(address)})", int)

    def data_quad_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283447>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.LittleEndian({fmt(address)})", int)

    def data_quad_long(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291876>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.Long({fmt(address)})", int)

    def data_quad_quad(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2292384>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.Quad({fmt(address)})", int)

    def data_quad_word(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291874>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Quad.Word({fmt(address)})", int)

    def data_sbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287960>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.SByte({fmt(address)})", int)

    def data_short(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287948>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Short({fmt(address)})", int)

    def data_short_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283429>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Short.BigEndian({fmt(address)})", int)

    def data_short_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283431>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Short.LittleEndian({fmt(address)})", int)

    def data_slong(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287962>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.SLong({fmt(address)})", int)

    def data_string(self, address: Address) -> str:
        """Get zero-terminated string with a maximum length

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1407362>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.STRing({fmt(address)})", str)

    def data_string_byte(self, address: Address) -> str:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"Data.STRing.Byte({fmt(address)})", str)

    def data_stringn(self, address: Address, length: int) -> str:
        """Get zero-terminated string with a maximum length

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1443823>`__.

        Args:
            address: Positional parameter 1
            length: Positional parameter 2
        """
        return self(f"Data.STRingN({fmt(address)}, {fmt(length)})", str)

    def data_sum(self) -> int:
        """Get checksum

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1443636>`__.
        """
        return self("Data.SUM()", int)

    def data_swap_long_byte(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768079>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Long.Byte({fmt(value)})", int)

    def data_swap_long_word(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768081>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Long.Word({fmt(value)})", int)

    def data_swap_quad_byte(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768084>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Quad.Byte({fmt(value)})", int)

    def data_swap_quad_long(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768088>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Quad.Long({fmt(value)})", int)

    def data_swap_quad_word(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768086>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Quad.Word({fmt(value)})", int)

    def data_swap_word_byte(self, value: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2768076>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"Data.SWAP.Word.Byte({fmt(value)})", int)

    def data_tbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287952>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.TByte({fmt(address)})", int)

    def data_word(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2287950>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Word({fmt(address)})", int)

    def data_word_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283433>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Word.BigEndian({fmt(address)})", int)

    def data_word_byte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291864>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Word.Byte({fmt(address)})", int)

    def data_word_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2283435>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Word.LittleEndian({fmt(address)})", int)

    def data_word_word(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2291865>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.Word.Word({fmt(address)})", int)

    def data_wstring(self, address: Address) -> str:
        """Get big-endian wide string

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2767573>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.WSTRING({fmt(address)})", str)

    def data_wstring_bigendian(self, address: Address) -> str:
        """Get big-endian wide string

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1857950>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.WSTRING.BigEndian({fmt(address)})", str)

    def data_wstring_littleendian(self, address: Address) -> str:
        """Get little-endian wide string

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1858033>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Data.WSTRING.LittleEndian({fmt(address)})", str)

    def date_date(self) -> str:
        """Current date

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573365>`__.
        """
        return self("DATE.DATE()", str)

    def date_day(self) -> int:
        """Today's date

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573367>`__.
        """
        return self("DATE.DAY()", int)

    def date_makeunixtime(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> int:
        """Date to Unix timestamp

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1367095>`__.

        Args:
            year: Positional parameter 1
            month: Positional parameter 2
            day: Positional parameter 3
            hour: Positional parameter 4
            minute: Positional parameter 5
            second: Positional parameter 6
        """
        return self(f"DATE.MakeUnixTime({fmt(year)}, {fmt(month)}, {fmt(day)}, {fmt(hour)}, {fmt(minute)}, {fmt(second)})", int)

    def date_month(self) -> int:
        """Number of current month

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1402538>`__.
        """
        return self("DATE.MONTH()", int)

    def date_seconds(self) -> int:
        """Seconds since midnight

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1619223>`__.
        """
        return self("DATE.SECONDS()", int)

    def date_time(self) -> str:
        """Current time

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1353811>`__.
        """
        return self("DATE.TIME()", str)

    def date_timezone(self) -> str:
        """Time zone identifier and hh:mm:ss

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1353883>`__.
        """
        return self("DATE.TimeZone()", str)

    def date_unixtime(self) -> int:
        """Seconds since Jan 1970

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1354070>`__.
        """
        return self("DATE.UnixTime()", int)

    def date_unixtimeus(self) -> int:
        """Microseconds since Jan 1970

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1861924>`__.
        """
        return self("DATE.UnixTimeUS()", int)

    def date_utcoffset(self) -> int:
        """Offset of current local time to UTC

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1639563>`__.
        """
        return self("DATE.utcOffset()", int)

    def date_year(self) -> int:
        """Current year

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1354223>`__.
        """
        return self("DATE.YEAR()", int)

    def debugger_feature(self, feature: str) -> bool:
        """Check debugger feature

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3035989>`__.

        Args:
            feature: Positional parameter 1
        """
        return self(f"DEBUGGER.FEATURE({fmt(feature)})", bool)

    def debugmode(self) -> str:
        """Current debug mode

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1159511>`__.
        """
        return self("DEBUGMODE()", str)

    def dialog_boolean(self, label: str) -> bool:
        """Current boolean value of checkbox

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573434>`__.

        Args:
            label: Positional parameter 1
        """
        return self(f"DIALOG.BOOLEAN({fmt(label)})", bool)

    def dialog_exist(self, label: str) -> bool:
        """Existence of dialog element

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1345715>`__.

        Args:
            label: Positional parameter 1
        """
        return self(f"DIALOG.EXIST({fmt(label)})", bool)

    def dialog_string(self, label: str) -> str:
        """Comma-separated list of values, e.g. from LISTBOX

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1346084>`__.

        Args:
            label: Positional parameter 1
        """
        return self(f"DIALOG.STRing({fmt(label)})", str)

    def dialog_string2(self, label: str) -> str:
        """Comma-separated list of values, e.g. from LISTBOX

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1346362>`__.

        Args:
            label: Positional parameter 1
        """
        return self(f"DIALOG.STRing2({fmt(label)})", str)

    def disassemble_address(self, address: Address) -> str:
        """Disassembled instruction at address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541468>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"DISASSEMBLE.ADDRESS({fmt(address)})", str)

    def dongleid(self, wibukey_index: int) -> int:
        """Serial number of USB WibuKey

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482862>`__.

        Args:
            wibukey_index: Positional parameter 1
        """
        return self(f"DONGLEID({fmt(wibukey_index)})", int)

    def dpp(self, register: int) -> int:
        """Content of DPP register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2421163>`__.

        Only available for C166.

        Args:
            register: Positional parameter 1
        """
        return self(f"DPP({fmt(register)})", int)

    def dwtbase(self) -> Address:
        """Only available for ARM.
        """
        return self("DWTBASE()", Address)

    def ela_version(self) -> int:
        """Only available for ARM, RISCV, XTENSA.
        """
        return self("ELA.VERSION()", int)

    def elabase(self) -> Address:
        """ELA base address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2038707>`__.

        Only available for ARM, RISCV, XTENSA.
        """
        return self("ELABASE()", Address)

    def epoc_dataaddress(self) -> int:
        """Start address of data area (EPOC debugger)

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482602>`__.

        Only available for ARM.
        """
        return self("EPOC.DATAADDRESS()", int)

    def epoc_entrypoint(self) -> int:
        """Entry address of debug task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482521>`__.

        Only available for ARM.
        """
        return self("EPOC.ENTRYPOINT()", int)

    def epoc_textaddress(self) -> int:
        """Start address of code area (EPOC debugger)

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1798587>`__.

        Only available for ARM.
        """
        return self("EPOC.TEXTADDRESS()", int)

    def error_address(self) -> Address:
        """Address of last occurred memory access error

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1543836>`__.
        """
        return self("ERROR.ADDRESS()", Address)

    def error_cmdline(self) -> str:
        """Erroneous command

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853715>`__.
        """
        return self("ERROR.CMDLINE()", str)

    def error_firstid(self) -> str:
        """ID of first error

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1844139>`__.
        """
        return self("ERROR.FIRSTID()", str)

    def error_id(self) -> str:
        """ID of last error message

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1852632>`__.
        """
        return self("ERROR.ID()", str)

    def error_message(self) -> str:
        """Error text

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1850523>`__.
        """
        return self("ERROR.MESSAGE()", str)

    def error_occurred(self) -> bool:
        """Error status

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1851268>`__.
        """
        return self("ERROR.OCCURRED()", bool)

    def error_position(self) -> int:
        """Error position

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1851305>`__.
        """
        return self("ERROR.POSITION()", int)

    def etb(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETB()", bool)

    def etbavailable(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBAVAILABLE()", bool)

    def etbbase(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBBASE()", Address)

    def etbcoresight(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBCORESIGHT()", bool)

    def etbfunnelavailable(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBFUNNELAVAILABLE()", bool)

    def etbfunnelbase(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBFUNNELBASE()", Address)

    def etbscorpion(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("ETBSCORPION()", bool)

    def etk(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2064310>`__.

        Only available for GTM, POWERPC, POWERPC64, TRICORE.
        """
        return self("ETK()", bool)

    def etm(self) -> bool:
        """TRUE if ETM trace is available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482192>`__.
        """
        return self("ETM()", bool)

    def etm_addrcomp(self) -> int:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482125>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.ADDRCOMP()", int)

    def etm_addrcomptotal(self) -> int:
        """Number of ETM address comparator pair

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482055>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.ADDRCOMPTOTAL()", int)

    def etm_contextcomp(self) -> int:
        """Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.CONTEXTCOMP()", int)

    def etm_counters(self) -> int:
        """Number of ETM counters

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481990>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.COUNTERS()", int)

    def etm_datacomp(self) -> int:
        """Number of ETM data comparators

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481974>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.DATACOMP()", int)

    def etm_extin(self) -> int:
        """Number of internal ETM inputs

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481809>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.EXTIN()", int)

    def etm_extout(self) -> int:
        """Number of external ETM outputs

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481746>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.EXTOUT()", int)

    def etm_fifofull(self) -> int:
        """ETM fifofull logic

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1797331>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.FIFOFULL()", int)

    def etm_map(self) -> int:
        """Number of ETM memory map decoders

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1797293>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.MAP()", int)

    def etm_protocol(self) -> int:
        """Version of ETM protocol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1797253>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.PROTOCOL()", int)

    def etm_sequencer(self) -> int:
        """Number of ETM sequencers

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481470>`__.

        Only available for ARM, CEVAX, OAK.
        """
        return self("ETM.SEQUENCER()", int)

    def etm_tracecore(self, number: int) -> bool:
        """Only available for ARM, CEVAX, OAK.

        Args:
            number: Positional parameter 1
        """
        return self(f"ETM.TraceCore({fmt(number)})", bool)

    def etm_version(self) -> int:
        """Only available for ARM, CEVAX, OAK, QDSP6, UBICOM32.
        """
        return self("ETM.VERSION()", int)

    def etmbase(self) -> Address:
        """Only available for ARM, CEVAX, OAK, QDSP6, UBICOM32.
        """
        return self("ETMBASE()", Address)

    def eval(self) -> int:
        """Value of expression evaluated with Eval command

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1639733>`__.
        """
        return self("EVAL()", int)

    def eval_address(self) -> Address:
        return self("EVAL.ADDRESS()", Address)

    def eval_boolean(self) -> bool:
        return self("EVAL.BOOLEAN()", bool)

    def eval_float(self) -> float:
        return self("EVAL.FLOAT()", float)

    def eval_param(self) -> str:
        return self("EVAL.PARAM()", str)

    def eval_string(self) -> str:
        """String composed by expression evaluated with Eval cmd.

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1639749>`__.
        """
        return self("EVAL.STRing()", str)

    def eval_time(self) -> float:
        """Value of time evaluated with Eval command

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1852998>`__.
        """
        return self("EVAL.TIme()", float)

    def eval_type(self) -> int:
        """Type of expression evaluated with Eval command

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1639771>`__.
        """
        return self("EVAL.TYPE()", int)

    def extended(self) -> bool:
        """TRUE if register CBAR > 0

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1481099>`__.

        Only available for Z80.
        """
        return self("EXTENDED()", bool)

    def false(self) -> bool:
        """Boolean expression

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342279>`__.
        """
        return self("FALSE()", bool)

    def fdx_instring(self, address: Address) -> str:
        """Content at FDX memory address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480985>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FDX.INSTRING({fmt(address)})", str)

    def fdx_records(self) -> int:
        return self("FDX.RECORDS()", int)

    def fdx_ref(self) -> int:
        return self("FDX.REF()", int)

    def fdx_state(self) -> int:
        return self("FDX.STATE()", int)

    def file_eof(self, file_number: int) -> bool:
        """Check if last read from file reached the end of the file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1351108>`__.

        Args:
            file_number: Positional parameter 1
        """
        return self(f"FILE.EOF({fmt(file_number)})", bool)

    def file_eoflastread(self) -> bool:
        """Check if last read from file reached the end of the file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1639953>`__.
        """
        return self("FILE.EOFLASTREAD()", bool)

    def file_exist(self, file: str) -> bool:
        """Check if file exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1351674>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"FILE.EXIST({fmt(file)})", bool)

    def file_open(self, file_number: int) -> bool:
        """Check if file is open

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1351781>`__.

        Args:
            file_number: Positional parameter 1
        """
        return self(f"FILE.OPEN({fmt(file_number)})", bool)

    def file_sum(self) -> str:
        """Get checksum from a file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1834358>`__.
        """
        return self("FILE.SUM()", str)

    def file_type(self, file: str) -> str:
        """File type of loaded file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1351873>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"FILE.TYPE({fmt(file)})", str)

    def flag(self) -> bool:
        """TRUE if hardware flag system available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480782>`__.
        """
        return self("FLAG()", bool)

    def flash_cfi_size(self, address: Address, bus_width: str) -> int:
        """Size of FLASH devices

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1510841>`__.

        Args:
            address: Positional parameter 1
            bus_width: Positional parameter 2
        """
        return self(f"FLASH.CFI.SIZE({fmt(address)}, {fmt(bus_width)})", int)

    def flash_cfi_width(self, address: Address) -> str:
        """Data bus width of FLASH devices

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2697297>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.CFI.WIDTH({fmt(address)})", str)

    def flash_clock_frequency(self) -> int:
        """FLASH clock value

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1510719>`__.
        """
        return self("FLASH.CLocK.Frequency()", int)

    def flash_id(self, id_type: str) -> int:
        """FLASH manufacturer and device ID

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2696187>`__.

        Args:
            id_type: Positional parameter 1
        """
        return self(f"FLASH.ID({fmt(id_type)})", int)

    def flash_list_state_pending(self) -> int:
        """Number of pending sectors

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1510584>`__.
        """
        return self("FLASH.List.STATE.PENDING()", int)

    def flash_list_type(self, address: Address) -> str:
        """FLASH family code of FLASH list entry

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2499705>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.List.TYPE({fmt(address)})", str)

    def flash_programmode(self) -> str:
        """FLASH programming modes

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2700732>`__.
        """
        return self("FLASH.ProgramMODE()", str)

    def flash_programmode_option(self) -> str:
        """FLASH programming options

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2702928>`__.
        """
        return self("FLASH.ProgramMODE.OPTION()", str)

    def flash_sector_begin(self, address: Address) -> Address:
        """Start address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1510046>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.BEGIN({fmt(address)})", Address)

    def flash_sector_end(self, address: Address) -> Address:
        """End address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1794737>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.END({fmt(address)})", Address)

    def flash_sector_exist(self, address: Address) -> bool:
        """TRUE if sector exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509856>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.EXIST({fmt(address)})", bool)

    def flash_sector_extravalue(self, address: Address) -> int:
        """Extra value of FLASH.Create

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2057953>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.EXTRAvalue({fmt(address)})", int)

    def flash_sector_next(self, address: Address) -> Address:
        """Address of next sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2058900>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.NEXT({fmt(address)})", Address)

    def flash_sector_option(self, address: Address, option_or_ALL: str) -> str:
        """Options of a FLASH sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2649599>`__.

        Args:
            address: Positional parameter 1
            option_or_ALL: Positional parameter 2
        """
        return self(f"FLASH.SECTOR.OPTION({fmt(address)}, {fmt(option_or_ALL)})", str)

    def flash_sector_otp(self, address: Address) -> bool:
        """TRUE if OTP sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509682>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.OTP({fmt(address)})", bool)

    def flash_sector_range(self, address: Address) -> AddressRange:
        """Address range of a FLASH sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2076142>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.RANGE({fmt(address)})", AddressRange)

    def flash_sector_size(self, address: Address) -> int:
        """Size in bytes

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509607>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.SIZE({fmt(address)})", int)

    def flash_sector_state(self, address: Address) -> str:
        """FLASH programming state

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509535>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.STATE({fmt(address)})", str)

    def flash_sector_type(self, address: Address) -> str:
        """FLASH family code of sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509377>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.TYPE({fmt(address)})", str)

    def flash_sector_width(self, address: Address) -> str:
        """Width of FLASH sector

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509282>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.SECTOR.WIDTH({fmt(address)})", str)

    def flash_spi_sfdp(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"FLASH.SPI.SFDP({fmt(string)})", str)

    def flash_target_build(self, file: str) -> int:
        """Build number of FLASH algorithm file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509201>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"FLASH.TARGET.BUILD({fmt(file)})", int)

    def flash_target_coderange(self) -> AddressRange:
        """Code range of FLASH algorithm

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2490145>`__.
        """
        return self("FLASH.TARGET.CODERANGE()", AddressRange)

    def flash_target_datarange(self) -> AddressRange:
        """Data range of FLASH algorithm

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2488187>`__.
        """
        return self("FLASH.TARGET.DATARANGE()", AddressRange)

    def flash_target_file(self) -> str:
        """Name of FLASH algorithm file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509127>`__.
        """
        return self("FLASH.TARGET.FILE()", str)

    def flash_target2_coderange(self) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2488285>`__.
        """
        return self("FLASH.TARGET2.CODERANGE()", AddressRange)

    def flash_target2_datarange(self) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2488311>`__.
        """
        return self("FLASH.TARGET2.DATARANGE()", AddressRange)

    def flash_target2_file(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2490526>`__.
        """
        return self("FLASH.TARGET2.FILE()", str)

    def flash_unit(self, address: Address) -> int:
        """Unit start address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1509023>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASH.UNIT({fmt(address)})", int)

    def flash_unit_begin(self, unit: int) -> Address:
        """Unit start address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1508942>`__.

        Args:
            unit: Positional parameter 1
        """
        return self(f"FLASH.UNIT.BEGIN({fmt(unit)})", Address)

    def flash_unit_end(self, unit: int) -> Address:
        """Unit end address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1508847>`__.

        Args:
            unit: Positional parameter 1
        """
        return self(f"FLASH.UNIT.END({fmt(unit)})", Address)

    def flash_unit_exist(self, unit: int) -> bool:
        """TRUE if unit exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1508751>`__.

        Args:
            unit: Positional parameter 1
        """
        return self(f"FLASH.UNIT.EXIST({fmt(unit)})", bool)

    def flash_unit_next(self, unit: int) -> int:
        """Number of next unit

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1508644>`__.

        Args:
            unit: Positional parameter 1
        """
        return self(f"FLASH.UNIT.NEXT({fmt(unit)})", int)

    def flashfile_getbadblock_count(self) -> int:
        """Number of bad blocks

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2494581>`__.
        """
        return self("FLASHFILE.GETBADBLOCK.COUNT()", int)

    def flashfile_getbadblock_next(self) -> int:
        """Address of bad block

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2494855>`__.
        """
        return self("FLASHFILE.GETBADBLOCK.NEXT()", int)

    def flashfile_spareaddress(self, address: int) -> int:
        """Address of spare area

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480553>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"FLASHFILE.SPAREADDRESS({fmt(address)})", int)

    def flashfile_spi_sfdp(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"FLASHFILE.SPI.SFDP({fmt(string)})", str)

    def flexnoc2trace_flow_errors(self) -> int:
        """Only available for ARM, CEVAX, XTENSA.
        """
        return self("FlexNoc2Trace.FLOW.ERRORS()", int)

    def flexnoc3trace_flow_errors(self) -> int:
        """Only available for ARM, CEVAX, XTENSA.
        """
        return self("FlexNoc3Trace.FLOW.ERRORS()", int)

    def flexnoctrace_flow_errors(self) -> int:
        """Only available for ARM, CEVAX, XTENSA.
        """
        return self("FlexNocTrace.FLOW.ERRORS()", int)

    def format_binary(self, width: int, number: int) -> str:
        """Numeric to binary value (leading spaces)

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573572>`__.

        Args:
            width: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"FORMAT.BINary({fmt(width)}, {fmt(number)})", str)

    def format_decimal(self, width: int, number: int) -> str:
        """Numeric to unsigned decimal as string (leading spaces)

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1374101>`__.

        Args:
            width: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"FORMAT.Decimal({fmt(width)}, {fmt(number)})", str)

    def format_decimalu(self, width: int, number: int) -> str:
        """Numeric to unsigned decimal as string (leading zeros)

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1374017>`__.

        Args:
            width: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"FORMAT.DecimalU({fmt(width)}, {fmt(number)})", str)

    def format_decimaluz(self, width: int, number: int) -> str:
        """Numeric to unsigned decimal as string (leading zeros)

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1622734>`__.

        Args:
            width: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"FORMAT.DecimalUZ({fmt(width)}, {fmt(number)})", str)

    def format_float(self, width: int, precision: int, number: float) -> str:
        """Floating point value to string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1373664>`__.

        Args:
            width: Positional parameter 1
            precision: Positional parameter 2
            number: Positional parameter 3
        """
        return self(f"FORMAT.FLOAT({fmt(width)}, {fmt(precision)}, {fmt(number)})", str)

    def format_hex(self, width: int, number: int) -> str:
        """Numeric to hex (leading zeros)

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1373412>`__.

        Args:
            width: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"FORMAT.HEX({fmt(width)}, {fmt(number)})", str)

    def format_unixtime(self, formatstr: str, timestamp: int, utc_offset: int) -> str:
        """Format Unix timestamps

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1359264>`__.

        Args:
            formatstr: Positional parameter 1
            timestamp: Positional parameter 2
            utc_offset: Positional parameter 3
        """
        return self(f"FORMAT.UnixTime({fmt(formatstr)}, {fmt(timestamp)}, {fmt(utc_offset)})", str)

    def found(self) -> bool:
        """TRUE() if search item was found

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1349434>`__.
        """
        return self("FOUND()", bool)

    def found_count(self) -> int:
        """Number of occurrences found

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1684611>`__.
        """
        return self("FOUND.COUNT()", int)

    def fpu(self, name: str) -> float:
        """FPU register contents

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480443>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"FPU({fmt(name)})", float)

    def fpu_raw(self, name: str) -> int:
        """FPU register raw contents

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2271024>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"FPU.RAW({fmt(name)})", int)

    def fpucr(self, name: str) -> int:
        """FPU control register contents

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480373>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"FPUCR({fmt(name)})", int)

    def funnel2available(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("FUNNEL2AVAILABLE()", bool)

    def funnel2base(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("FUNNEL2BASE()", Address)

    def funnelavailable(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("FUNNELAVAILABLE()", bool)

    def funnelbase(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("FUNNELBASE()", Address)

    def fxu(self, register_name: str) -> str:
        """Content of FXU register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2194769>`__.

        Only available for V800.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"FXU({fmt(register_name)})", str)

    def gdb_port(self) -> int:
        """Port number for communication via GDB interface

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1312417>`__.
        """
        return self("GDB.PORT()", int)

    def gdtb(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("GDTB()", int)

    def gdtl(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("GDTL()", int)

    def group_exist(self, group_name: str) -> bool:
        """TRUE if group exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480267>`__.

        Args:
            group_name: Positional parameter 1
        """
        return self(f"GROUP.EXIST({fmt(group_name)})", bool)

    def hardware_combiprobe(self) -> bool:
        """TRUE if CombiProbe is connected

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541521>`__.
        """
        return self("hardware.COMBIPROBE()", bool)

    def hardware_esi(self) -> bool:
        """TRUE if ESI hardware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1482264>`__.
        """
        return self("hardware.ESI()", bool)

    def hardware_fire(self) -> bool:
        return self("hardware.FIRE()", bool)

    def hardware_icd(self) -> bool:
        """TRUE if universal base module is connected

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541557>`__.
        """
        return self("hardware.ICD()", bool)

    def hardware_ice(self) -> bool:
        return self("hardware.ICE()", bool)

    def hardware_lcp(self) -> bool:
        return self("hardware.LCP()", bool)

    def hardware_powerdebug(self) -> bool:
        """TRUE if PowerDebug or PowerTrace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1642998>`__.
        """
        return self("hardware.POWERDEBUG()", bool)

    def hardware_powerintegrator(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495550>`__.
        """
        return self("hardware.POWERINTEGRATOR()", bool)

    def hardware_powerintegrator2(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495648>`__.
        """
        return self("hardware.POWERINTEGRATOR2()", bool)

    def hardware_powernexus(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495422>`__.
        """
        return self("hardware.POWERNEXUS()", bool)

    def hardware_powerprobe(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1496784>`__.
        """
        return self("hardware.POWERPROBE()", bool)

    def hardware_powertrace(self) -> bool:
        """Adapter name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495360>`__.
        """
        return self("hardware.POWERTRACE()", bool)

    def hardware_powertrace2(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1776517>`__.
        """
        return self("hardware.POWERTRACE2()", bool)

    def hardware_powertrace2lite(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2772653>`__.
        """
        return self("hardware.POWERTRACE2LITE()", bool)

    def hardware_powertrace3(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2969076>`__.
        """
        return self("hardware.POWERTRACE3()", bool)

    def hardware_powertracepx(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2174377>`__.
        """
        return self("hardware.POWERTRACEPX()", bool)

    def hardware_powertraceserial(self) -> bool:
        """Adapter name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2048984>`__.
        """
        return self("hardware.POWERTRACESERIAL()", bool)

    def hardware_powertraceserial_adapter_name(self) -> str:
        """Adapter name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2716952>`__.
        """
        return self("hardware.POWERTRACESERIAL.ADAPTER.NAME()", str)

    def hardware_powertraceserial_adapter_rev(self) -> int:
        """Adapter revision

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2717153>`__.
        """
        return self("hardware.POWERTRACESERIAL.ADAPTER.REV()", int)

    def hardware_scu(self) -> bool:
        """TRUE if PodBus Ethernet Controller is used

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1480222>`__.
        """
        return self("hardware.SCU()", bool)

    def hardware_stg(self) -> bool:
        """TRUE if Stimuli Generator hardware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1451204>`__.
        """
        return self("hardware.STG()", bool)

    def hardware_ta32(self) -> bool:
        """TRUE if TA32 is available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1449315>`__.
        """
        return self("hardware.TA32()", bool)

    def hardware_utrace(self) -> bool:
        """TRUE if debugger is a uTrace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1479969>`__.
        """
        return self("hardware.UTRACE()", bool)

    def headid(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2068087>`__.
        """
        return self("HEADID()", int)

    def help_filter(self) -> str:
        return self("HELP.Filter()", str)

    def help_message(self) -> str:
        """Help search item

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1349779>`__.
        """
        return self("HELP.MESSAGE()", str)

    def hostid(self) -> int:
        """Host ID

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1349917>`__.
        """
        return self("HOSTID()", int)

    def hostip(self) -> int:
        """Host IP address

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853676>`__.
        """
        return self("HOSTIP()", int)

    def htm(self) -> bool:
        """Only available for ARM, CEVAX, IPU, OAK, RISCV, STRED.
        """
        return self("HTM()", bool)

    def htmbase(self) -> Address:
        """Only available for ARM, CEVAX, IPU, OAK, RISCV, STRED.
        """
        return self("HTMBASE()", Address)

    def hvx(self, register_name: str) -> str:
        """Content of HVX register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1479686>`__.

        Only available for QDSP6.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"HVX({fmt(register_name)})", str)

    def i2c_data(self, index: int) -> int:
        """Data read by I2C.TRANSFER

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1479467>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"I2C.DATA({fmt(index)})", int)

    def i2c_pin(self, pin_name: str) -> int:
        """Pin status

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1479389>`__.

        Args:
            pin_name: Positional parameter 1
        """
        return self(f"I2C.PIN({fmt(pin_name)})", int)

    def id_cable(self) -> int:
        """Hardware ID of debug cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1410362>`__.
        """
        return self("ID.CABLE()", int)

    def id_powertraceauxport(self) -> int:
        return self("ID.POWERTRACEAUXPORT()", int)

    def id_preprocessor(self) -> int:
        """Hardware ID of preprocessor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1791325>`__.
        """
        return self("ID.PREPROcessor()", int)

    def id_whisker(self, number: int) -> int:
        """ID of whisker cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1674973>`__.

        Args:
            number: Positional parameter 1
        """
        return self(f"ID.WHISKER({fmt(number)})", int)

    def idcode(self, n: int) -> int:
        """Number of detected TAPs

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1410408>`__.

        Args:
            n: Positional parameter 1
        """
        return self(f"IDCODE({fmt(n)})", int)

    def idcodenumber(self) -> int:
        """Number of detected TAPs

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1410429>`__.
        """
        return self("IDCODENUMBER()", int)

    def idtb(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("IDTB()", int)

    def idtl(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("IDTL()", int)

    def ifconfig_collisions(self) -> int:
        """Collisions since start-up

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573673>`__.
        """
        return self("IFCONFIG.COLLISIONS()", int)

    def ifconfig_configuration(self) -> str:
        """Connection type

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1376238>`__.
        """
        return self("IFCONFIG.CONFIGURATION()", str)

    def ifconfig_devicename(self) -> str:
        """Name of TRACE32 device

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1375752>`__.
        """
        return self("IFCONFIG.DEVICENAME()", str)

    def ifconfig_errors(self) -> int:
        """Errors since start-up

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1376029>`__.
        """
        return self("IFCONFIG.ERRORS()", int)

    def ifconfig_ethernetaddress(self) -> int:
        """MAC address of TRACE32 device

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853604>`__.
        """
        return self("IFCONFIG.ETHernetADDRESS()", int)

    def ifconfig_ipaddress(self) -> str:
        """IP address of TRACE32 device

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1853563>`__.
        """
        return self("IFCONFIG.IPADDRESS()", str)

    def ifconfig_resyncs(self) -> int:
        """Resyncs since start-up

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1375187>`__.
        """
        return self("IFCONFIG.RESYNCS()", int)

    def ifconfig_retries(self) -> int:
        """Retries since start-up

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1375031>`__.
        """
        return self("IFCONFIG.RETRIES()", int)

    def iftest_download(self) -> int:
        """Download in KByte/sec

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1374533>`__.
        """
        return self("IFTEST.DOWNLOAD()", int)

    def iftest_latency(self) -> float:
        """Latency in microseconds

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1374734>`__.
        """
        return self("IFTEST.LATENCY()", float)

    def iftest_upload(self) -> int:
        """Upload in KByte/sec

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1376668>`__.
        """
        return self("IFTEST.UPLOAD()", int)

    def integrator(self) -> bool:
        """TRUE if PowerIntegrator

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516874>`__.
        """
        return self("Integrator()", bool)

    def integrator_adc_enable(self, channel: str) -> bool:
        """Bitmask of enabled analog channels

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516807>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"Integrator.ADC.ENABLE({fmt(channel)})", bool)

    def integrator_adc_shunt(self, channel: str) -> float:
        """Shunt-resistor value

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516736>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"Integrator.ADC.SHUNT({fmt(channel)})", float)

    def integrator_analog(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516664>`__.
        """
        return self("Integrator.ANALOG()", int)

    def integrator_counter_event(self, counter_name: str) -> int:
        """Get value of trigger program event counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2208155>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"Integrator.COUNTER.EVENT({fmt(counter_name)})", int)

    def integrator_counter_extern(self, counter_name: str) -> int:
        """Value of trigger program external counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516515>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"Integrator.COUNTER.EXTERN({fmt(counter_name)})", int)

    def integrator_counter_time(self, counter_name: str) -> float:
        """Get value of trigger program time counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1516434>`__.

        Args:
            counter_name: Positional parameter 1
        """
        return self(f"Integrator.COUNTER.TIME({fmt(counter_name)})", float)

    def integrator_dialogdsel(self, string: str) -> int:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541814>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"Integrator.DIALOGDSEL({fmt(string)})", int)

    def integrator_dialogdselget(self, string: str) -> str:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1512383>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"Integrator.DIALOGDSELGET({fmt(string)})", str)

    def integrator_dsel(self) -> str:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1512320>`__.
        """
        return self("Integrator.DSEL()", str)

    def integrator_find_pi_channel(self, signal_name: str) -> int:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1512190>`__.

        Args:
            signal_name: Positional parameter 1
        """
        return self(f"Integrator.FIND.PI_CHANNEL({fmt(signal_name)})", int)

    def integrator_find_pi_word(self, signal_word: str) -> bool:
        """TRUE if signal word is defined

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1512121>`__.

        Args:
            signal_word: Positional parameter 1
        """
        return self(f"Integrator.FIND.PI_WORD({fmt(signal_word)})", bool)

    def integrator_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853519>`__.
        """
        return self("Integrator.FIRST()", int)

    def integrator_flag(self, flag_name: str) -> bool:
        """Check state of trigger program FLAG

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1512060>`__.

        Args:
            flag_name: Positional parameter 1
        """
        return self(f"Integrator.FLAG({fmt(flag_name)})", bool)

    def integrator_get(self, channel_name: str) -> int:
        """Value of channel

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511917>`__.

        Args:
            channel_name: Positional parameter 1
        """
        return self(f"Integrator.GET({fmt(channel_name)})", int)

    def integrator_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511860>`__.
        """
        return self("Integrator.MAXSIZE()", int)

    def integrator_probe(self) -> int:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2460094>`__.
        """
        return self("Integrator.PROBE()", int)

    def integrator_programfilename(self) -> str:
        """File name of trigger program

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511746>`__.
        """
        return self("Integrator.PROGRAMFILENAME()", str)

    def integrator_record_data(self, record_number: int, channel: str) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511683>`__.

        Args:
            record_number: Positional parameter 1
            channel: Positional parameter 2
        """
        return self(f"Integrator.RECORD.DATA({fmt(record_number)}, {fmt(channel)})", int)

    def integrator_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511619>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Integrator.RECORD.TIME({fmt(record_number)})", float)

    def integrator_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511552>`__.
        """
        return self("Integrator.RECORDS()", int)

    def integrator_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511491>`__.
        """
        return self("Integrator.REF()", int)

    def integrator_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511418>`__.
        """
        return self("Integrator.SIZE()", int)

    def integrator_state(self) -> int:
        """Get state of the Integrator

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511292>`__.
        """
        return self("Integrator.STATE()", int)

    def integrator_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511230>`__.
        """
        return self("Integrator.TRACK.RECORD()", int)

    def integrator_usb(self) -> int:
        """For internal usage only

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1511164>`__.
        """
        return self("Integrator.USB()", int)

    def intercom_getglobalmacro(self, name_or_host_port: str, macroname: str) -> str:
        """Exchange strings between PowerView instances

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1871023>`__.

        Args:
            name_or_host_port: Positional parameter 1
            macroname: Positional parameter 2
        """
        return self(f"InterCom.GetGlobalMacro({fmt(name_or_host_port)}, {fmt(macroname)})", str)

    def intercom_getpracticestate(self, intercom_name_or_host_and_port_number: str) -> str:
        """PRACTICE run-state on other instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1870286>`__.

        Args:
            intercom_name_or_host_and_port_number: Positional parameter 1
        """
        return self(f"InterCom.GetPracticeState({fmt(intercom_name_or_host_and_port_number)})", str)

    def intercom_name(self) -> str:
        """InterCom name of this TRACE32 instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1869390>`__.
        """
        return self("InterCom.NAME()", str)

    def intercom_ping(self, intercom_name_or_host_and_port_number: str) -> bool:
        """Check if ping is successful

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573739>`__.

        Args:
            intercom_name_or_host_and_port_number: Positional parameter 1
        """
        return self(f"InterCom.PING({fmt(intercom_name_or_host_and_port_number)})", bool)

    def intercom_podport(self, index: int) -> int:
        """InterCom name of any TRACE32 instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1350546>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"InterCom.PODPORT({fmt(index)})", int)

    def intercom_podportname(self, index: int) -> str:
        """InterCom name of any TRACE32 instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1821253>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"InterCom.PODPORTNAME({fmt(index)})", str)

    def intercom_podportnumber(self) -> int:
        """Number of TRACE32 instances

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1350639>`__.
        """
        return self("InterCom.PODPORTNUMBER()", int)

    def intercom_port(self) -> int:
        """Port number of this TRACE32 instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1312793>`__.
        """
        return self("InterCom.PORT()", int)

    def interface_cadi(self) -> bool:
        """TRUE if connection to target is via CADI interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1505251>`__.
        """
        return self("INTERFACE.CADI()", bool)

    def interface_das(self) -> bool:
        return self("interface.DAS()", bool)

    def interface_gdb(self) -> bool:
        """TRUE if connection to target is via GDB interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1505190>`__.
        """
        return self("INTERFACE.GDB()", bool)

    def interface_gdi(self) -> bool:
        return self("interface.GDI()", bool)

    def interface_host(self) -> bool:
        """TRUE if application is debugged on host

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1505046>`__.
        """
        return self("INTERFACE.HOST()", bool)

    def interface_hostmci(self) -> bool:
        """TRUE if TRACE32 debug driver runs on host

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504953>`__.
        """
        return self("interface.HOSTMCI()", bool)

    def interface_iris(self) -> bool:
        """TRUE if connection to target is via IRIS interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2689184>`__.
        """
        return self("INTERFACE.IRIS()", bool)

    def interface_mcd(self) -> bool:
        """TRUE if connection to target via MCD interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504889>`__.
        """
        return self("INTERFACE.MCD()", bool)

    def interface_name(self) -> str:
        """Name of debugger

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1984031>`__.
        """
        return self("INTERFACE.NAME()", str)

    def interface_qnx(self) -> bool:
        """TRUE if PBI=QNX

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1983985>`__.
        """
        return self("INTERFACE.QNX()", bool)

    def interface_sim(self) -> bool:
        """TRUE if simulator

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504760>`__.
        """
        return self("INTERFACE.SIM()", bool)

    def interface_vast(self) -> bool:
        """TRUE if connection to target via VAST interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504703>`__.
        """
        return self("INTERFACE.VAST()", bool)

    def interface_vdi(self) -> bool:
        """TRUE if connection to target via Virtio interface

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504637>`__.
        """
        return self("INTERFACE.VDI()", bool)

    def iobase(self) -> int:
        """Base address of internal I/O's

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541857>`__.

        Only available for I386, I386_64, M68HC16, M68K, MCORE, MIPS, MIPS64, OAK, PCP, POWERPC, POWERPC64, SC100, Z80.
        """
        return self("IOBASE()", int)

    def iobase_address(self) -> Address:
        """Base address of internal I/O's with access class

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1410154>`__.

        Only available for I386, I386_64, M68HC16, M68K, MCORE, MIPS, MIPS64, OAK, PCP, POWERPC, POWERPC64, SC100, Z80.
        """
        return self("IOBASE.ADDRESS()", Address)

    def iprobe(self) -> bool:
        """TRUE if IPROBE

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1497632>`__.
        """
        return self("IProbe()", bool)

    def iprobe_adc_enable(self, channel: str) -> bool:
        """TRUE if channel is enabled

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1145311>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"IProbe.ADC.ENABLE({fmt(channel)})", bool)

    def iprobe_adc_shunt(self, channel: str) -> float:
        """Shunt resistor value of channel

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1145419>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"IProbe.ADC.SHUNT({fmt(channel)})", float)

    def iprobe_analog(self) -> bool:
        """TRUE if Analog Probe is plugged

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1498364>`__.
        """
        return self("IProbe.ANALOG()", bool)

    def iprobe_digital(self) -> bool:
        return self("IProbe.DIGITAL()", bool)

    def iprobe_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853365>`__.
        """
        return self("IProbe.FIRST()", int)

    def iprobe_get(self, channel_name: str) -> int:
        """Value of channel

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1498228>`__.

        Args:
            channel_name: Positional parameter 1
        """
        return self(f"IProbe.GET({fmt(channel_name)})", int)

    def iprobe_getanalog(self, string: str) -> float:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"IProbe.GETAnalog({fmt(string)})", float)

    def iprobe_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1498161>`__.
        """
        return self("IProbe.MAXSIZE()", int)

    def iprobe_probe(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1498084>`__.
        """
        return self("IProbe.PROBE()", bool)

    def iprobe_record_data(self, record_number: int, channel: str) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1498011>`__.

        Args:
            record_number: Positional parameter 1
            channel: Positional parameter 2
        """
        return self(f"IProbe.RECORD.DATA({fmt(record_number)}, {fmt(channel)})", int)

    def iprobe_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1497939>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"IProbe.RECORD.TIME({fmt(record_number)})", float)

    def iprobe_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1497755>`__.
        """
        return self("IProbe.RECORDS()", int)

    def iprobe_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1137780>`__.
        """
        return self("IProbe.REF()", int)

    def iprobe_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1137601>`__.
        """
        return self("IProbe.SIZE()", int)

    def iprobe_state(self) -> int:
        """Get state of IProbe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1786871>`__.
        """
        return self("IProbe.STATE()", int)

    def iprobe_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1142819>`__.
        """
        return self("IProbe.TRACK.RECORD()", int)

    def ipt(self) -> bool:
        """Only available for I386, I386_64.
        """
        return self("IPT()", bool)

    def ipt_rtit(self) -> bool:
        """Only available for I386, I386_64.
        """
        return self("IPT.RTIT()", bool)

    def itm(self) -> bool:
        """Only available for ARM.
        """
        return self("ITM()", bool)

    def itmbase(self, number: int) -> Address:
        """Only available for ARM.

        Args:
            number: Positional parameter 1
        """
        return self(f"ITMBASE({fmt(number)})", Address)

    def jtag_mipi34(self, pin: str) -> int:
        """Query special MIPI34 pins

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2744403>`__.

        Args:
            pin: Positional parameter 1
        """
        return self(f"JTAG.MIPI34({fmt(pin)})", int)

    def jtag_ontrigger_state(self) -> int:
        """Only available for ARM.
        """
        return self("JTAG.ONTRIGGER.STATE()", int)

    def jtag_pin(self, signal_name: str) -> int:
        """Level of JTAG signal

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2744383>`__.

        Args:
            signal_name: Positional parameter 1
        """
        return self(f"JTAG.PIN({fmt(signal_name)})", int)

    def jtag_sequence_exist(self, seq_name: str) -> bool:
        """Check if a JTAG sequence exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2548889>`__.

        Only available for ARC, ARM, CEVAX, OAK, RISCV, SDMA, TRICORE, V800, XTENSA.

        Args:
            seq_name: Positional parameter 1
        """
        return self(f"JTAG.SEQuence.EXIST({fmt(seq_name)})", bool)

    def jtag_sequence_locked(self, seq_name: str) -> bool:
        """Check if a JTAG sequence is locked

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2548914>`__.

        Only available for ARC, ARM, CEVAX, OAK, RISCV, SDMA, TRICORE, V800, XTENSA.

        Args:
            seq_name: Positional parameter 1
        """
        return self(f"JTAG.SEQuence.LOCKED({fmt(seq_name)})", bool)

    def jtag_sequence_result(self, global_seq_variable: int) -> int:
        """Get result of JTAG sequence

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2548859>`__.

        Only available for ARC, ARM, CEVAX, OAK, RISCV, SDMA, TRICORE, V800, XTENSA.

        Args:
            global_seq_variable: Positional parameter 1
        """
        return self(f"JTAG.SEQuence.RESULT({fmt(global_seq_variable)})", int)

    def jtag_shift(self) -> int:
        """TDO output of JTAG shift

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478968>`__.
        """
        return self("JTAG.SHIFT()", int)

    def jtag_x7efuse_cntl(self) -> int:
        """CNTL flags read by JTAG.X7EFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1977623>`__.
        """
        return self("JTAG.X7EFUSE.CNTL()", int)

    def jtag_x7efuse_dna(self) -> int:
        """DNA value read by JTAG.X7EFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2081773>`__.
        """
        return self("JTAG.X7EFUSE.DNA()", int)

    def jtag_x7efuse_key(self) -> str:
        """AES key read by JTAG.X7EFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1975377>`__.
        """
        return self("JTAG.X7EFUSE.KEY()", str)

    def jtag_x7efuse_result(self) -> int:
        """Result of JTAG.X7EFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1972992>`__.
        """
        return self("JTAG.X7EFUSE.RESULT()", int)

    def jtag_x7efuse_user(self) -> int:
        """User code read by JTAG.X7EFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1975763>`__.
        """
        return self("JTAG.X7EFUSE.USER()", int)

    def jtag_xusefuse_cntl(self) -> int:
        """CNTL value read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2678017>`__.
        """
        return self("JTAG.XUSEFUSE.CNTL()", int)

    def jtag_xusefuse_dna(self) -> str:
        """DNA value read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2678681>`__.
        """
        return self("JTAG.XUSEFUSE.DNA()", str)

    def jtag_xusefuse_key(self) -> str:
        """AES key read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2679132>`__.
        """
        return self("JTAG.XUSEFUSE.KEY()", str)

    def jtag_xusefuse_result(self) -> int:
        """Result of JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2677482>`__.
        """
        return self("JTAG.XUSEFUSE.RESULT()", int)

    def jtag_xusefuse_rsa(self) -> str:
        """RSA hash read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2680025>`__.
        """
        return self("JTAG.XUSEFUSE.RSA()", str)

    def jtag_xusefuse_sec(self) -> int:
        """SEC value read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2680573>`__.
        """
        return self("JTAG.XUSEFUSE.SEC()", int)

    def jtag_xusefuse_user(self) -> int:
        """User code read by JTAG.XUSEFUSE command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2680892>`__.
        """
        return self("JTAG.XUSEFUSE.USER()", int)

    def jtag_xusefuse_user128(self) -> str:
        """128 bit User code read by JTAG.XUSEFUSE

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2681280>`__.
        """
        return self("JTAG.XUSEFUSE.USER128()", str)

    def la(self) -> bool:
        return self("LA()", bool)

    def la_maxsize(self) -> int:
        return self("LA.MAXSIZE()", int)

    def la_records(self) -> int:
        return self("LA.RECORDS()", int)

    def la_ref(self) -> int:
        return self("LA.REF()", int)

    def la_size(self) -> int:
        return self("LA.SIZE()", int)

    def la_state(self) -> int:
        return self("LA.STATE()", int)

    def language(self) -> str:
        return self("LANGUAGE()", str)

    def license_date(self, index: int) -> str:
        """Expiration date of maintenance contract

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573819>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"LICENSE.DATE({fmt(index)})", str)

    def license_family(self, index: int) -> str:
        """Name of the CPU family license

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1320160>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"LICENSE.FAMILY({fmt(index)})", str)

    def license_features(self, index: int) -> str:
        """List of features licensed

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1320296>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"LICENSE.FEATURES({fmt(index)})", str)

    def license_getindex(self) -> int:
        """Index of maintenance contract

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1320421>`__.
        """
        return self("LICENSE.getINDEX()", int)

    def license_granted(self, product: str, version: str) -> int:
        """License state

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1320520>`__.

        Args:
            product: Positional parameter 1
            version: Positional parameter 2
        """
        return self(f"LICENSE.GRANTED({fmt(product)}, {fmt(version)})", int)

    def license_havefeature(self, name: str) -> bool:
        """Checks if license is stored in debugger hardware

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640177>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"LICENSE.HAVEFEATURE({fmt(name)})", bool)

    def license_mserial(self, index: int) -> str:
        """Serial number of the maintenance contract

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1348648>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"LICENSE.MSERIAL({fmt(index)})", str)

    def license_multicore(self) -> bool:
        """Check if multicore debugging is licensed

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1348550>`__.
        """
        return self("LICENSE.MULTICORE()", bool)

    def license_requiredforcpu(self) -> str:
        """License required for selected CPU

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1878530>`__.
        """
        return self("LICENSE.RequiredForCPU()", str)

    def license_serial(self, index: int) -> str:
        """Serial number of debug cable

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1877663>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"LICENSE.SERIAL({fmt(index)})", str)

    def log_do_file(self) -> str:
        """Get log file used by LOG.DO

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1834697>`__.
        """
        return self("LOG.DO.FILE()", str)

    def logger_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853695>`__.
        """
        return self("LOGGER.FIRST()", int)

    def logger_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478869>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"LOGGER.RECORD.ADDRESS({fmt(record_number)})", Address)

    def logger_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478772>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"LOGGER.RECORD.DATA({fmt(record_number)})", int)

    def logger_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478674>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"LOGGER.RECORD.OFFSET({fmt(record_number)})", int)

    def logger_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478587>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"LOGGER.RECORD.TIME({fmt(record_number)})", float)

    def logger_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478463>`__.
        """
        return self("LOGGER.RECORDS()", int)

    def logger_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478402>`__.
        """
        return self("LOGGER.REF()", int)

    def logger_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478316>`__.
        """
        return self("LOGGER.SIZE()", int)

    def logger_state(self) -> int:
        """Get state of Logger trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1478030>`__.
        """
        return self("LOGGER.STATE()", int)

    def macho_lastuuid(self) -> str:
        """Universally unique identifier of MachO file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477891>`__.

        Only available for ARM, I386, I386_64.
        """
        return self("MACHO.LASTUUID()", str)

    def map_romsize(self) -> int:
        """Size of the defined ROM

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477685>`__.
        """
        return self("MAP.ROMSIZE()", int)

    def math_abs(self, integer: int) -> int:
        """Absolute value of decimal value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573943>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"math.ABS({fmt(integer)})", int)

    def math_fabs(self, float_number: float) -> float:
        """Absolute value of floating point number

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1573945>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FABS({fmt(float_number)})", float)

    def math_fcos(self, float_number: float) -> float:
        """Cosine of an angle given in radian

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640266>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FCOS({fmt(float_number)})", float)

    def math_fexp(self, float_number: float) -> float:
        """Exponentiation with base 10

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640317>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FEXP({fmt(float_number)})", float)

    def math_fexp10(self, float_number: float) -> float:
        """Exponentiation with base 10

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640426>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FEXP10({fmt(float_number)})", float)

    def math_finf(self) -> float:
        """Positive infinity

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1335397>`__.
        """
        return self("math.FINF()", float)

    def math_flog(self, float_number: float) -> float:
        """Logarithm to base 10 of given value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640485>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FLOG({fmt(float_number)})", float)

    def math_flog10(self, float_number: float) -> float:
        """Logarithm to base 10 of given value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640588>`__.

        Args:
            float_number: Positional parameter 1
        """
        return self(f"math.FLOG10({fmt(float_number)})", float)

    def math_fmax(self, float1: float, float2: float) -> float:
        """Return the larger one of two floating point values

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1421057>`__.

        Args:
            float1: Positional parameter 1
            float2: Positional parameter 2
        """
        return self(f"math.FMAX({fmt(float1)}, {fmt(float2)})", float)

    def math_fmin(self, float1: float, float2: float) -> float:
        """Return the smaller one of two floating point values

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1421088>`__.

        Args:
            float1: Positional parameter 1
            float2: Positional parameter 2
        """
        return self(f"math.FMIN({fmt(float1)}, {fmt(float2)})", float)

    def math_fmod(self, x: float, y: float) -> float:
        """Floating-Point Modulus

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1881358>`__.

        Args:
            x: Positional parameter 1
            y: Positional parameter 2
        """
        return self(f"math.FMOD({fmt(x)}, {fmt(y)})", float)

    def math_fnan(self) -> float:
        """Not a number value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1335925>`__.
        """
        return self("math.FNAN()", float)

    def math_fpow(self, float_x: float, float_y: float) -> float:
        """Y-th power of base x

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1336799>`__.

        Args:
            float_x: Positional parameter 1
            float_y: Positional parameter 2
        """
        return self(f"math.FPOW({fmt(float_x)}, {fmt(float_y)})", float)

    def math_fsin(self, value: float) -> float:
        """Sine of an angle given in radian

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1335945>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"math.FSIN({fmt(value)})", float)

    def math_fsqrt(self, value: float) -> float:
        """Square-root of given value

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1640710>`__.

        Args:
            value: Positional parameter 1
        """
        return self(f"math.FSQRT({fmt(value)})", float)

    def math_max(self, integer1: int, integer2: int) -> int:
        """Return the larger one of two decimal values

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1421201>`__.

        Args:
            integer1: Positional parameter 1
            integer2: Positional parameter 2
        """
        return self(f"math.MAX({fmt(integer1)}, {fmt(integer2)})", int)

    def math_min(self, integer1: int, integer2: int) -> int:
        """Return the smaller one of two decimal values

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1421221>`__.

        Args:
            integer1: Positional parameter 1
            integer2: Positional parameter 2
        """
        return self(f"math.MIN({fmt(integer1)}, {fmt(integer2)})", int)

    def math_sign(self, integer: int) -> int:
        """Return -1 or 0 or +1 depending on argument

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1454264>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"math.SIGN({fmt(integer)})", int)

    def math_signum(self, integer: int) -> int:
        """Return -1 or 0 or +1 depending on argument

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1336079>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"math.SIGNUM({fmt(integer)})", int)

    def mcds_module_name(self) -> str:
        """Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.Module.NAME()", str)

    def mcds_module_number(self) -> int:
        """Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.Module.NUMBER()", int)

    def mcds_module_revision(self) -> int:
        """Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.Module.REVision()", int)

    def mcds_module_type(self) -> int:
        """Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.Module.TYPE()", int)

    def mcds_state(self) -> int:
        """MCDS module is switched on/off

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477368>`__.

        Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.STATE()", int)

    def mcds_tracebuffer_lowergap(self) -> int:
        """Trace buffer lower gap

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2081335>`__.

        Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.TraceBuffer.LowerGAP()", int)

    def mcds_tracebuffer_size(self) -> int:
        """Trace buffer size

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477239>`__.

        Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.TraceBuffer.SIZE()", int)

    def mcds_tracebuffer_uppergap(self) -> int:
        """Trace buffer upper gap

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477169>`__.

        Only available for C166, GTM, PCP, TRICORE.
        """
        return self("MCDS.TraceBuffer.UpperGAP()", int)

    def menu_exist(self, name: str) -> bool:
        """Check if menu name exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1923993>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"MENU.EXIST({fmt(name)})", bool)

    def mmu(self, register_name: str) -> int:
        """Value of MMU register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541904>`__.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"MMU({fmt(register_name)})", int)

    def mmu_defaultpt(self) -> Address:
        """Base address of default page table

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2662716>`__.
        """
        return self("MMU.DEFAULTPT()", Address)

    def mmu_defaultpt_zone(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2663303>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.DEFAULTPT.ZONE({fmt(address)})", Address)

    def mmu_defaultpt2(self) -> Address:
        """Only available for M68K, MIPS, MIPS64.
        """
        return self("MMU.DEFAULTPT2()", Address)

    def mmu_defaulttrans_logrange(self) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2641126>`__.
        """
        return self("MMU.DEFAULTTRANS.LOGRANGE()", AddressRange)

    def mmu_defaulttrans_logrange_zone(self, address: Address) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2641130>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.DEFAULTTRANS.LOGRANGE.ZONE({fmt(address)})", AddressRange)

    def mmu_defaulttrans_physaddr(self) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2641127>`__.
        """
        return self("MMU.DEFAULTTRANS.PHYSADDR()", Address)

    def mmu_defaulttrans_physaddr_zone(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2641131>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.DEFAULTTRANS.PHYSADDR.ZONE({fmt(address)})", Address)

    def mmu_format(self) -> str:
        """Currently selected MMU format

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1477058>`__.
        """
        return self("MMU.FORMAT()", str)

    def mmu_format_detected(self) -> str:
        """Auto-detection of page table format

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2670156>`__.

        Only available for I386, I386_64, RISCV.
        """
        return self("MMU.FORMAT.DETECTED()", str)

    def mmu_format_detected_zone(self, address: Address) -> str:
        """Auto-detection of page table format

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2625655>`__.

        Only available for I386, I386_64, RISCV.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.FORMAT.DETECTED.ZONE({fmt(address)})", str)

    def mmu_format_zone(self, address: Address) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2664537>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.FORMAT.ZONE({fmt(address)})", str)

    def mmu_intermediate(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2270694>`__.

        Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.INTERMEDIATE({fmt(address)})", Address)

    def mmu_intermediate_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2092812>`__.

        Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.INTERMEDIATE.VALID({fmt(address)})", bool)

    def mmu_intermediateex(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2738189>`__.

        Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.INTERMEDIATEEX({fmt(address)})", Address)

    def mmu_intermediateex_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2738100>`__.

        Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.INTERMEDIATEEX.VALID({fmt(address)})", bool)

    def mmu_linear(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2092856>`__.

        Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.LINEAR({fmt(address)})", Address)

    def mmu_linear_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2204215>`__.

        Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.LINEAR.VALID({fmt(address)})", bool)

    def mmu_linearex(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2737982>`__.

        Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.LINEAREX({fmt(address)})", Address)

    def mmu_linearex_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2737912>`__.

        Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.LINEAREX.VALID({fmt(address)})", bool)

    def mmu_list_logrange(self, number: int) -> AddressRange:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"MMU.LIST.LOGRANGE({fmt(number)})", AddressRange)

    def mmu_list_logrange_zone(self, number: int, address: Address) -> AddressRange:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"MMU.LIST.LOGRANGE.ZONE({fmt(number)}, {fmt(address)})", AddressRange)

    def mmu_list_number(self) -> int:
        return self("MMU.LIST.NUMBER()", int)

    def mmu_list_number_zone(self, address: Address) -> int:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.LIST.NUMBER.ZONE({fmt(address)})", int)

    def mmu_list_physaddr(self, number: int) -> Address:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"MMU.LIST.PHYSADDR({fmt(number)})", Address)

    def mmu_list_physaddr_zone(self, number: int, address: Address) -> Address:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"MMU.LIST.PHYSADDR.ZONE({fmt(number)}, {fmt(address)})", Address)

    def mmu_list_type(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"MMU.LIST.TYPE({fmt(number)})", str)

    def mmu_list_type_zone(self, number: int, address: Address) -> str:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"MMU.LIST.TYPE.ZONE({fmt(number)}, {fmt(address)})", str)

    def mmu_logical(self, physical_address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2727979>`__.

        Args:
            physical_address: Positional parameter 1
        """
        return self(f"MMU.LOGICAL({fmt(physical_address)})", Address)

    def mmu_logical_valid(self, physical_address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2092977>`__.

        Args:
            physical_address: Positional parameter 1
        """
        return self(f"MMU.LOGICAL.VALID({fmt(physical_address)})", bool)

    def mmu_physical(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2736935>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.PHYSICAL({fmt(address)})", Address)

    def mmu_physical_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2093095>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.PHYSICAL.VALID({fmt(address)})", bool)

    def mmu_physicalex(self, address: Address) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2736974>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.PHYSICALEX({fmt(address)})", Address)

    def mmu_physicalex_valid(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2738210>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.PHYSICALEX.VALID({fmt(address)})", bool)

    def mmu_vtlb_numupdatedentries(self, address: Address) -> int:
        """Only available for QDSP6.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.VTLB.NUMUPDATEDENTRIES({fmt(address)})", int)

    def mmu_vtlb_revisionctr(self, address: Address) -> int:
        """Only available for QDSP6.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.VTLB.REVISIONCTR({fmt(address)})", int)

    def mmu_vtlb_updatemode(self, address: Address) -> str:
        """Only available for QDSP6.

        Args:
            address: Positional parameter 1
        """
        return self(f"MMU.VTLB.UPDATEMODE({fmt(address)})", str)

    def mmx(self, register_name: str) -> int:
        """Value of MMX register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1475655>`__.

        Only available for ARM, I386, I386_64.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"MMX({fmt(register_name)})", int)

    def monitor(self) -> bool:
        """TRUE if debugger is running as monitor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1475740>`__.
        """
        return self("MONITOR()", bool)

    def nexus(self) -> bool:
        """TRUE if Nexus trace is supported

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472921>`__.

        Only available for ARC, AVR32, ETPU, GTM, POWERPC, POWERPC64, V800.
        """
        return self("NEXUS()", bool)

    def nexus_portmode(self) -> str:
        """Current PortMode setting

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472721>`__.

        Only available for ARC, AVR32, ETPU, GTM, POWERPC, POWERPC64, V800.
        """
        return self("NEXUS.PortMode()", str)

    def nexus_portsize(self) -> str:
        """Current PortSize setting

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472749>`__.

        Only available for ARC, AVR32, ETPU, GTM, POWERPC, POWERPC64, V800.
        """
        return self("NEXUS.PortSize()", str)

    def nexus_rttbuild(self, register_index: int) -> int:
        """RTT build register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2506273>`__.

        Only available for ARC.

        Args:
            register_index: Positional parameter 1
        """
        return self(f"NEXUS.RTTBUILD({fmt(register_index)})", int)

    def nodename(self) -> str:
        """Node name of connected TRACE32 device

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342096>`__.
        """
        return self("NODENAME()", str)

    def ocpbase(self) -> Address:
        """Only available for ARM, C5000, C6000, C7000_64.
        """
        return self("OCPBASE()", Address)

    def ocptype(self) -> int:
        """Only available for ARM, C5000, C6000, C7000_64.
        """
        return self("OCPTYPE()", int)

    def onchip(self) -> bool:
        """TRUE if the onchip trace is available

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2069519>`__.
        """
        return self("Onchip()", bool)

    def onchip_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853634>`__.
        """
        return self("Onchip.FIRST()", int)

    def onchip_flow_errors(self) -> int:
        """Get number of flow errors / hard errors

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1474191>`__.
        """
        return self("Onchip.FLOW.ERRORS()", int)

    def onchip_flow_fifofull(self) -> int:
        """Get number of FIFO overflows

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2208626>`__.
        """
        return self("Onchip.FLOW.FIFOFULL()", int)

    def onchip_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1474013>`__.
        """
        return self("Onchip.MAXSIZE()", int)

    def onchip_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473933>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Onchip.RECORD.ADDRESS({fmt(record_number)})", Address)

    def onchip_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473851>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Onchip.RECORD.DATA({fmt(record_number)})", int)

    def onchip_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473762>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Onchip.RECORD.OFFSET({fmt(record_number)})", int)

    def onchip_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473667>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Onchip.RECORD.TIME({fmt(record_number)})", float)

    def onchip_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473600>`__.
        """
        return self("Onchip.RECORDS()", int)

    def onchip_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473519>`__.
        """
        return self("Onchip.REF()", int)

    def onchip_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473457>`__.
        """
        return self("Onchip.SIZE()", int)

    def onchip_state(self) -> int:
        """Get state of Onchip trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1473078>`__.
        """
        return self("Onchip.STATE()", int)

    def onchip_traceconnect(self) -> str:
        """Name of trace sink of the SoC

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2171837>`__.
        """
        return self("Onchip.TraceCONNECT()", str)

    def onchip_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472994>`__.
        """
        return self("Onchip.TRACK.RECORD()", int)

    def os_dir(self, directory_name: str) -> bool:
        """Access rights to directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1572052>`__.

        Args:
            directory_name: Positional parameter 1
        """
        return self(f"OS.DIR({fmt(directory_name)})", bool)

    def os_dir_access(self, directory_name: str, access_right: str) -> bool:
        """Access rights to directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1396055>`__.

        Args:
            directory_name: Positional parameter 1
            access_right: Positional parameter 2
        """
        return self(f"OS.DIR.ACCESS({fmt(directory_name)}, {fmt(access_right)})", bool)

    def os_env(self, env_var: str) -> str:
        """Value of OS environment variable

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1577067>`__.

        Args:
            env_var: Positional parameter 1
        """
        return self(f"OS.ENV({fmt(env_var)})", str)

    def os_file_abspath(self, file: str) -> str:
        """Absolute path to file or directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1529580>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.ABSPATH({fmt(file)})", str)

    def os_file_access(self, file: str, access_type: str) -> bool:
        """Access rights to file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1396213>`__.

        Args:
            file: Positional parameter 1
            access_type: Positional parameter 2
        """
        return self(f"OS.FILE.ACCESS({fmt(file)}, {fmt(access_type)})", bool)

    def os_file_basename(self, path: str, suffix: str) -> str:
        """Strip directory and suffix from filenames

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1859174>`__.

        Args:
            path: Positional parameter 1
            suffix: Positional parameter 2
        """
        return self(f"OS.FILE.BASENAME({fmt(path)}, {fmt(suffix)})", str)

    def os_file_date(self, file: str) -> str:
        """Modification date of file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1858380>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.DATE({fmt(file)})", str)

    def os_file_date2(self, file: str) -> str:
        """Modification date of file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1454362>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.DATE2({fmt(file)})", str)

    def os_file_exist(self, file: str) -> bool:
        """Check if file exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1860002>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.EXIST({fmt(file)})", bool)

    def os_file_extension(self, file: str) -> str:
        """File name extension

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1387348>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.EXTENSION({fmt(file)})", str)

    def os_file_joinpath(self, path1: str, path2: str, path3: str, path4: str, path5: str, path6: str) -> str:
        """Join multiple paths

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1872293>`__.

        Args:
            path1: Positional parameter 1
            path2: Positional parameter 2
            path3: Positional parameter 3
            path4: Positional parameter 4
            path5: Positional parameter 5
            path6: Positional parameter 6
        """
        return self(f"OS.FILE.JOINPATH({fmt(path1)}, {fmt(path2)}, {fmt(path3)}, {fmt(path4)}, {fmt(path5)}, {fmt(path6)})", str)

    def os_file_link(self, file: str) -> str:
        """Real file name of file link

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1874165>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.LINK({fmt(file)})", str)

    def os_file_name(self, path: str) -> str:
        """Extract file name from path

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1225836>`__.

        Args:
            path: Positional parameter 1
        """
        return self(f"OS.FILE.NAME({fmt(path)})", str)

    def os_file_path(self, file: str) -> str:
        """Return path of file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1386877>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.PATH({fmt(file)})", str)

    def os_file_readable(self, file: str) -> bool:
        """Check if file can be opened for reading

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1860308>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.readable({fmt(file)})", bool)

    def os_file_realpath(self, file: str) -> str:
        """Canonical absolute path to file or directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1529635>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.REALPATH({fmt(file)})", str)

    def os_file_size(self, file: str) -> int:
        """File size in bytes

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1386767>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.SIZE({fmt(file)})", int)

    def os_file_time(self, file: str) -> str:
        """Modification timestamp of file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1386625>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.TIME({fmt(file)})", str)

    def os_file_unixtime(self, file: str) -> int:
        """Unix timestamp of file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1339700>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"OS.FILE.UnixTime({fmt(file)})", int)

    def os_firstfile(self, string1: str, string2: str) -> str:
        """First file name matching a pattern

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1269679>`__.

        Args:
            string1: Positional parameter 1
            string2: Positional parameter 2
        """
        return self(f"OS.FIRSTFILE({fmt(string1)}, {fmt(string2)})", str)

    def os_id(self) -> str:
        """User ID of TRACE32 instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1388262>`__.
        """
        return self("OS.ID()", str)

    def os_name(self) -> str:
        """Basic name of operating system

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1371970>`__.
        """
        return self("OS.NAME()", str)

    def os_nextfile(self) -> str:
        """Next file name matching a pattern

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1389393>`__.
        """
        return self("OS.NEXTFILE()", str)

    def os_portavailable_tcp(self, port_number: int) -> bool:
        """Check if TCP port is used

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1821384>`__.

        Args:
            port_number: Positional parameter 1
        """
        return self(f"OS.PORTAVAILABLE.TCP({fmt(port_number)})", bool)

    def os_portavailable_udp(self, port_number: int) -> bool:
        """Check if UDP port is used

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1821405>`__.

        Args:
            port_number: Positional parameter 1
        """
        return self(f"OS.PORTAVAILABLE.UDP({fmt(port_number)})", bool)

    def os_presentconfigurationfile(self) -> str:
        """Name of used TRACE32 configuration file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1386020>`__.
        """
        return self("OS.PresentConfigurationFile()", str)

    def os_presentdemodirectory(self) -> str:
        """Demo directory for the current architecture

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1385727>`__.
        """
        return self("OS.PresentDemoDirectory()", str)

    def os_presentexecutabledirectory(self) -> str:
        """Directory of current TRACE32 exe.

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1385563>`__.
        """
        return self("OS.PresentExecutableDirectory()", str)

    def os_presentexecutablefile(self) -> str:
        """Path and file name of current TRACE32 exe.

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1795125>`__.
        """
        return self("OS.PresentExecutableFile()", str)

    def os_presenthelpdirectory(self) -> str:
        """Path of the TRACE32 online help directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1378530>`__.
        """
        return self("OS.PresentHELPDirectory()", str)

    def os_presenthomedirectory(self) -> str:
        """Path of the home directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1378703>`__.
        """
        return self("OS.PresentHomeDirectory()", str)

    def os_presentlicensefile(self) -> str:
        """Current TRACE32 license file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1378418>`__.
        """
        return self("OS.PresentLicenseFile()", str)

    def os_presentpracticedirectory(self) -> str:
        """Directory of currently executed script

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1807614>`__.
        """
        return self("OS.PresentPracticeDirectory()", str)

    def os_presentpracticefile(self) -> str:
        """Path and file name of currently executed script

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1807307>`__.
        """
        return self("OS.PresentPracticeFile()", str)

    def os_presentsystemdirectory(self) -> str:
        """TRACE32 system directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1378095>`__.
        """
        return self("OS.PresentSystemDirectory()", str)

    def os_presenttemporarydirectory(self) -> str:
        """TRACE32 temporary directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1377967>`__.
        """
        return self("OS.PresentTemporaryDirectory()", str)

    def os_presentworkingdirectory(self) -> str:
        """Current working directory

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1377842>`__.
        """
        return self("OS.PresentWorkingDirectory()", str)

    def os_return(self) -> int:
        """Return code of the last executed operating system command

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1377194>`__.
        """
        return self("OS.RETURN()", int)

    def os_timer(self) -> int:
        """OS timer in milliseconds

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1377131>`__.
        """
        return self("OS.TIMER()", int)

    def os_tmpfile(self) -> str:
        """Name for a temporary file

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1216524>`__.
        """
        return self("OS.TMPFILE()", str)

    def os_version(self, version_data_type: int) -> int:
        """Type of the host operating system

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1233628>`__.

        Args:
            version_data_type: Positional parameter 1
        """
        return self(f"OS.VERSION({fmt(version_data_type)})", int)

    def os_window_line(self, WinTOP_or_window_name: str, line: int) -> str:
        """Get line from an OS.Window window

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1856543>`__.

        Args:
            WinTOP_or_window_name: Positional parameter 1
            line: Positional parameter 2
        """
        return self(f"OS.Window.LINE({fmt(WinTOP_or_window_name)}, {fmt(line)})", str)

    def path_number(self) -> int:
        """Number of path entries

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1832581>`__.
        """
        return self("PATH.NUMBER()", int)

    def path_path(self, index: int) -> str:
        """Search path entry

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1832649>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PATH.PATH({fmt(index)})", str)

    def pattern(self) -> bool:
        return self("PATTERN()", bool)

    def pbi(self) -> str:
        return self("PBI()", str)

    def pci_read_b(self, bus: int, device: int, function: int, register: int) -> int:
        """Byte from PCI register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1517171>`__.

        Only available for I386, I386_64.

        Args:
            bus: Positional parameter 1
            device: Positional parameter 2
            function: Positional parameter 3
            register: Positional parameter 4
        """
        return self(f"PCI.Read.B({fmt(bus)}, {fmt(device)}, {fmt(function)}, {fmt(register)})", int)

    def pci_read_l(self, bus: int, device: int, function: int, register: int) -> int:
        """Long from PCI register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1541951>`__.

        Only available for I386, I386_64.

        Args:
            bus: Positional parameter 1
            device: Positional parameter 2
            function: Positional parameter 3
            register: Positional parameter 4
        """
        return self(f"PCI.Read.L({fmt(bus)}, {fmt(device)}, {fmt(function)}, {fmt(register)})", int)

    def pci_read_w(self, bus: int, device: int, function: int, register: int) -> int:
        """Word from PCI register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1517393>`__.

        Only available for I386, I386_64.

        Args:
            bus: Positional parameter 1
            device: Positional parameter 2
            function: Positional parameter 3
            register: Positional parameter 4
        """
        return self(f"PCI.Read.W({fmt(bus)}, {fmt(device)}, {fmt(function)}, {fmt(register)})", int)

    def per_address_isnonsecure(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2982629>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.ADDRESS.isNONSECURE({fmt(address)})", bool)

    def per_address_isnonsecureex(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2982631>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.ADDRESS.isNONSECUREEX({fmt(address)})", bool)

    def per_address_issecure(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2982633>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.ADDRESS.isSECURE({fmt(address)})", bool)

    def per_address_issecureex(self, address: Address) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2982635>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.ADDRESS.isSECUREEX({fmt(address)})", bool)

    def per_arg(self) -> int:
        """Argument of PER.view command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2982603>`__.
        """
        return self("PER.ARG()", int)

    def per_arg_address(self) -> Address:
        """Address argument of PER.view command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2975840>`__.
        """
        return self("PER.ARG.ADDRESS()", Address)

    def per_autoindent(self) -> bool:
        return self("PER.AutoIndent()", bool)

    def per_buffer_byte(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034483>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.Byte({fmt(index)})", int)

    def per_buffer_long(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034576>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.Long({fmt(index)})", int)

    def per_buffer_longlong(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034603>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.LongLong({fmt(index)})", int)

    def per_buffer_quad(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034598>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.Quad({fmt(index)})", int)

    def per_buffer_short(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034555>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.Short({fmt(index)})", int)

    def per_buffer_word(self, index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034514>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PER.Buffer.Word({fmt(index)})", int)

    def per_byte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2049152>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Byte({fmt(address)})", int)

    def per_errorline(self) -> str:
        return self("PER.ERRORLINE()", str)

    def per_eval(self, integer: int) -> Address:
        """Value of expression in PER file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504548>`__.

        Args:
            integer: Positional parameter 1
        """
        return self(f"PER.EVAL({fmt(integer)})", Address)

    def per_filename(self) -> str:
        """PER file name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2975807>`__.
        """
        return self("PER.FILENAME()", str)

    def per_hbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034669>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.HByte({fmt(address)})", int)

    def per_long(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034665>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Long({fmt(address)})", int)

    def per_long_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034799>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Long.BigEndian({fmt(address)})", int)

    def per_long_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034801>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Long.LittleEndian({fmt(address)})", int)

    def per_longlong(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034677>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.LongLong({fmt(address)})", int)

    def per_longlong_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034803>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.LongLong.BigEndian({fmt(address)})", int)

    def per_longlong_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034805>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.LongLong.LittleEndian({fmt(address)})", int)

    def per_pbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034667>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.PByte({fmt(address)})", int)

    def per_quad(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034675>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Quad({fmt(address)})", int)

    def per_quad_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034807>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Quad.BigEndian({fmt(address)})", int)

    def per_quad_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034809>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Quad.LittleEndian({fmt(address)})", int)

    def per_sbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034671>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.SByte({fmt(address)})", int)

    def per_short(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2049154>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Short({fmt(address)})", int)

    def per_short_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034791>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Short.BigEndian({fmt(address)})", int)

    def per_short_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034793>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Short.LittleEndian({fmt(address)})", int)

    def per_slong(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034673>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.SLong({fmt(address)})", int)

    def per_tbyte(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034663>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.TByte({fmt(address)})", int)

    def per_word(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034661>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Word({fmt(address)})", int)

    def per_word_bigendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034795>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Word.BigEndian({fmt(address)})", int)

    def per_word_littleendian(self, address: Address) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2034797>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"PER.Word.LittleEndian({fmt(address)})", int)

    def perf_memory_hits(self, value: int, core: int) -> int:
        """Number of memory samples

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1503706>`__.

        Args:
            value: Positional parameter 1
            core: Positional parameter 2
        """
        return self(f"PERF.MEMORY.HITS({fmt(value)}, {fmt(core)})", int)

    def perf_memory_snoopaddress(self) -> Address:
        """Snoop memory address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1503630>`__.
        """
        return self("PERF.MEMORY.SnoopAddress()", Address)

    def perf_memory_snoopsize(self) -> int:
        """Snoop size

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1503550>`__.
        """
        return self("PERF.MEMORY.SnoopSize()", int)

    def perf_method(self) -> int:
        """Recording method

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1503270>`__.
        """
        return self("PERF.METHOD()", int)

    def perf_mode(self) -> int:
        return self("PERF.Mode()", int)

    def perf_pc_hits(self, address_range: AddressRange, core: int) -> int:
        """Number of PC samples

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502879>`__.

        Args:
            address_range: Positional parameter 1
            core: Positional parameter 2
        """
        return self(f"PERF.PC.HITS({fmt(address_range)}, {fmt(core)})", int)

    def perf_rate(self) -> int:
        """Number of snoops per second

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502801>`__.
        """
        return self("PERF.RATE()", int)

    def perf_runtime(self) -> str:
        """Retained time for program run

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502714>`__.
        """
        return self("PERF.RunTime()", str)

    def perf_snoopfails(self) -> int:
        """Number of snoop fails

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502633>`__.
        """
        return self("PERF.SNOOPFAILS()", int)

    def perf_state(self) -> int:
        """Get state of Performance Analyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502333>`__.
        """
        return self("PERF.STATE()", int)

    def perf_task_hits(self, task_magic: int, core: int) -> int:
        """Number of task samples

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1502243>`__.

        Args:
            task_magic: Positional parameter 1
            core: Positional parameter 2
        """
        return self(f"PERF.TASK.HITS({fmt(task_magic)}, {fmt(core)})", int)

    def pmibase(self) -> Address:
        """Only available for ARM, C6000, C7000_64.
        """
        return self("PMIBASE()", Address)

    def port_get(self, channel_name: str) -> int:
        """Value of channel

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2841694>`__.

        Args:
            channel_name: Positional parameter 1
        """
        return self(f"PORT.GET({fmt(channel_name)})", int)

    def port_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1475470>`__.
        """
        return self("PORT.MAXSIZE()", int)

    def port_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1475341>`__.
        """
        return self("PORT.RECORDS()", int)

    def port_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1780794>`__.
        """
        return self("PORT.REF()", int)

    def port_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2214484>`__.
        """
        return self("PORT.SIZE()", int)

    def port_state(self) -> int:
        """Get state of Port Analyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1474684>`__.
        """
        return self("PORT.STATE()", int)

    def port_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1474622>`__.
        """
        return self("PORT.TRACK.RECORD()", int)

    def portanalyzer(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542086>`__.
        """
        return self("PORTANALYZER()", bool)

    def portsharing(self) -> int:
        """Current setting of PortSHaRing

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2064297>`__.

        Only available for ARM, GTM, PCP, POWERPC, POWERPC64, TRICORE, V800.
        """
        return self("PORTSHARING()", int)

    def pp(self) -> Address:
        """Address of program pointer (access class, space ID, program counter)

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1373285>`__.
        """
        return self("PP()", Address)

    def practice_arg(self, argument_index: int) -> str:
        """Number of passed or returned arguments

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1574016>`__.

        Args:
            argument_index: Positional parameter 1
        """
        return self(f"PRACTICE.ARG({fmt(argument_index)})", str)

    def practice_arg_size(self) -> int:
        """Number of passed or returned arguments

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1512861>`__.
        """
        return self("PRACTICE.ARG.SIZE()", int)

    def practice_caller_file(self, index: int) -> str:
        """File name of the script/subscript caller

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1406080>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PRACTICE.CALLER.FILE({fmt(index)})", str)

    def practice_caller_line(self, index: int) -> int:
        """Line number in caller script

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1407170>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"PRACTICE.CALLER.LINE({fmt(index)})", int)

    def practice_command_available(self, command: str) -> bool:
        """Check if command is available

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1407060>`__.

        Args:
            command: Positional parameter 1
        """
        return self(f"PRACTICE.CoMmanD.AVAILable({fmt(command)})", bool)

    def practice_function_available(self, function: str) -> bool:
        """Check if function is available

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1338259>`__.

        Args:
            function: Positional parameter 1
        """
        return self(f"PRACTICE.FUNCtion.AVAILable({fmt(function)})", bool)

    def practice_stackdepth(self) -> int:
        return self("PRACTICE.StackDepth()", int)

    def printer_filename(self) -> str:
        """Path and file name of next print operation

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1567489>`__.
        """
        return self("PRINTER.FILENAME()", str)

    def probe(self) -> bool:
        return self("Probe()", bool)

    def probe_counter_event(self, string: str) -> int:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Probe.COUNTER.EVENT({fmt(string)})", int)

    def probe_counter_extern(self, string: str) -> int:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Probe.COUNTER.EXTERN({fmt(string)})", int)

    def probe_counter_time(self, string: str) -> float:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Probe.COUNTER.TIME({fmt(string)})", float)

    def probe_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1853303>`__.
        """
        return self("Probe.FIRST()", int)

    def probe_flag(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Probe.FLAG({fmt(string)})", bool)

    def probe_get(self, channel_name: str) -> int:
        """Value of channel

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1496361>`__.

        Args:
            channel_name: Positional parameter 1
        """
        return self(f"PROBE.GET({fmt(channel_name)})", int)

    def probe_maxsize(self) -> int:
        return self("Probe.MAXSIZE()", int)

    def probe_record_data(self, number: int, string: str) -> int:
        """
        Args:
            number: Positional parameter 1
            string: Positional parameter 2
        """
        return self(f"Probe.RECORD.DATA({fmt(number)}, {fmt(string)})", int)

    def probe_record_time(self, number: int) -> float:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"Probe.RECORD.TIME({fmt(number)})", float)

    def probe_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1496091>`__.
        """
        return self("PROBE.RECORDS()", int)

    def probe_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495996>`__.
        """
        return self("PROBE.REF()", int)

    def probe_size(self) -> int:
        return self("Probe.SIZE()", int)

    def probe_state(self) -> int:
        """Get state of PowerProbe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495804>`__.
        """
        return self("PROBE.STATE()", int)

    def probe_track_record(self) -> int:
        """Get record number matching search

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1495732>`__.
        """
        return self("PROBE.TRACK.RECORD()", int)

    def processid(self) -> int:
        """Process identifier of a TRACE32 PowerView instance

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1416501>`__.
        """
        return self("ProcessID()", int)

    def python_running(self) -> int:
        return self("PYthon.RUNNING()", int)

    def python_terminal_line(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"PYthon.TERMinal.LINE({fmt(number)})", str)

    def radix(self) -> int:
        """Current radix setting

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1346746>`__.
        """
        return self("RADIX()", int)

    def random(self) -> int:
        """Pseudo random number

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1630248>`__.
        """
        return self("RANDOM()", int)

    def random_range(self, min: int, max: int) -> int:
        """Pseudo hex random number from specified range

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1353198>`__.

        Args:
            min: Positional parameter 1
            max: Positional parameter 2
        """
        return self(f"RANDOM.RANGE({fmt(min)}, {fmt(max)})", int)

    def random_range_hex(self, min: int, max: int) -> int:
        """Pseudo hex random number from specified range

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1867074>`__.

        Args:
            min: Positional parameter 1
            max: Positional parameter 2
        """
        return self(f"RANDOM.RANGE.HEX({fmt(min)}, {fmt(max)})", int)

    def rcl_port(self, index: int) -> int:
        """UDP Port number of remote API interface

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1344544>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"RCL.PORT({fmt(index)})", int)

    def rcl_tcp_port(self) -> int:
        """TCP Port number of remote API interface

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1866049>`__.
        """
        return self("RCL.TCP.PORT()", int)

    def register(self, register_name_or_PP: str) -> int:
        """First / next register name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1373635>`__.

        Args:
            register_name_or_PP: Positional parameter 1
        """
        return self(f"Register({fmt(register_name_or_PP)})", int)

    def register_list(self, register_name: str) -> str:
        """First / next register name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1399775>`__.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"Register.LIST({fmt(register_name)})", str)

    def rtpbase(self) -> Address:
        """Only available for ARM.
        """
        return self("RTPBASE()", Address)

    def rts_busy(self) -> bool:
        """Check if RTS is busy

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2757874>`__.
        """
        return self("RTS.BUSY()", bool)

    def rts_error(self) -> bool:
        """Check for flowerrors during RTS processing

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1409401>`__.
        """
        return self("RTS.ERROR()", bool)

    def rts_fifofull(self) -> bool:
        """Check for FIFO full error in RTS

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2758516>`__.
        """
        return self("RTS.FIFOFULL()", bool)

    def rts_nocode(self) -> bool:
        """Check for RTS NOCODE error

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2757700>`__.
        """
        return self("RTS.NOCODE()", bool)

    def rts_record(self) -> int:
        """Find record causing an error in RTS

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2758050>`__.
        """
        return self("RTS.RECORD()", int)

    def rts_records(self) -> int:
        """Get number of trace records transferred to RTS

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2192153>`__.
        """
        return self("RTS.RECORDS()", int)

    def runtime_accuracy(self) -> float:
        """Accuracy of run-time counter

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542563>`__.
        """
        return self("RunTime.ACCURACY()", float)

    def runtime_actual(self) -> float:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1409547>`__.
        """
        return self("RunTime.ACTUAL()", float)

    def runtime_last(self) -> float:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1409618>`__.
        """
        return self("RunTime.LAST()", float)

    def runtime_lastrun(self) -> float:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542595>`__.
        """
        return self("RunTime.LASTRUN()", float)

    def runtime_refa(self) -> float:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1409679>`__.
        """
        return self("RunTime.REFA()", float)

    def runtime_refb(self) -> float:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1409742>`__.
        """
        return self("RunTime.REFB()", float)

    def sdtibase(self) -> Address:
        """Only available for ARM, C5000, C6000, C7000_64.
        """
        return self("SDTIBASE()", Address)

    def selection_address(self) -> Address:
        return self("SELECTION.ADDRESS()", Address)

    def selection_string(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2092722>`__.
        """
        return self("SELECTION.STRing()", str)

    def simulator(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1504796>`__.
        """
        return self("SIMULATOR()", bool)

    def smmu_baseaddress(self, smmu_name: str) -> Address:
        """Base address of SMMU

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1396574>`__.

        Only available for ARM.

        Args:
            smmu_name: Positional parameter 1
        """
        return self(f"SMMU.BaseADDRESS({fmt(smmu_name)})", Address)

    def smmu_streamid2smrg(self, string: str, number: int) -> int:
        """Only available for ARM.

        Args:
            string: Positional parameter 1
            number: Positional parameter 2
        """
        return self(f"SMMU.Streamid2SMRG({fmt(string)}, {fmt(number)})", int)

    def snooper_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2208048>`__.
        """
        return self("SNOOPer.FIRST()", int)

    def snooper_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472494>`__.
        """
        return self("SNOOPer.MAXSIZE()", int)

    def snooper_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472386>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"SNOOPer.RECORD.ADDRESS({fmt(record_number)})", Address)

    def snooper_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472299>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"SNOOPer.RECORD.DATA({fmt(record_number)})", int)

    def snooper_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472205>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"SNOOPer.RECORD.OFFSET({fmt(record_number)})", int)

    def snooper_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1472090>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"SNOOPer.RECORD.TIME({fmt(record_number)})", float)

    def snooper_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1471852>`__.
        """
        return self("SNOOPer.RECORDS()", int)

    def snooper_ref(self) -> int:
        """Get record number of reference record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1471947>`__.
        """
        return self("SNOOPer.REF()", int)

    def snooper_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1471783>`__.
        """
        return self("SNOOPer.SIZE()", int)

    def snooper_state(self) -> int:
        """Get state of SNOOPer trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1471473>`__.
        """
        return self("SNOOPer.STATE()", int)

    def software_64bit(self) -> bool:
        """Check if TRACE32 executable is 64-bit

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1574130>`__.
        """
        return self("SOFTWARE.64BIT()", bool)

    def software_build(self) -> int:
        """Upper build number

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1519352>`__.
        """
        return self("SOFTWARE.BUILD()", int)

    def software_build_base(self) -> int:
        """Lower build number

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1352721>`__.
        """
        return self("SOFTWARE.BUILD.BASE()", int)

    def software_scubased(self) -> bool:
        return self("SOFTWARE.SCUBASED()", bool)

    def software_version(self) -> str:
        """Release build or nightly build, etc.

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1352907>`__.
        """
        return self("SOFTWARE.VERSION()", str)

    def spe(self, register_name: str) -> int:
        """Content from SPE register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1450859>`__.

        Only available for POWERPC, POWERPC64.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"SPE({fmt(register_name)})", int)

    def sse(self, register_name_dot_column_number: str) -> int:
        """Segment from SSE register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1450982>`__.

        Only available for I386, I386_64.

        Args:
            register_name_dot_column_number: Positional parameter 1
        """
        return self(f"SSE({fmt(register_name_dot_column_number)})", int)

    def state_halt(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1470489>`__.
        """
        return self("STATE.HALT()", bool)

    def state_monitor_run(self) -> bool:
        return self("STATE.MONITOR.RUN()", bool)

    def state_nocpuaccess(self) -> bool:
        """See `Armv8-A/R and Armv9 Debugger <https://www.lauterbach.com/pdf/debugger_armv8v9.pdf#G6640122>`__.

        Only available for ARM.
        """
        return self("STATE.NOCPUACCESS()", bool)

    def state_noctiaccess(self) -> bool:
        """See `Armv8-A/R and Armv9 Debugger <https://www.lauterbach.com/pdf/debugger_armv8v9.pdf#G7514914>`__.

        Only available for ARM.
        """
        return self("STATE.NOCTIACCESS()", bool)

    def state_oslk(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1660738>`__.

        Only available for ARM.
        """
        return self("STATE.OSLK()", bool)

    def state_power(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1138444>`__.
        """
        return self("STATE.POWER()", bool)

    def state_processor(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1469914>`__.
        """
        return self("STATE.PROCESSOR()", str)

    def state_reset(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1469845>`__.
        """
        return self("STATE.RESET()", bool)

    def state_run(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1469812>`__.
        """
        return self("STATE.RUN()", bool)

    def state_target(self) -> str:
        """State of target displayed in TRACE32 state line

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1469673>`__.
        """
        return self("STATE.TARGET()", str)

    def step_diverge_reachedtarget(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"Step.Diverge.ReachedTarget({fmt(address)})", bool)

    def stmbase(self) -> Address:
        """Only available for ARC, ARM, C5000, C6000, C7000_64, CEVAX, I386, I386_64, NIOS, QDSP6, RISCV, STRED.
        """
        return self("STMBASE()", Address)

    def string_char(self, string: str, index: int) -> int:
        """Extract a character

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1574190>`__.

        Args:
            string: Positional parameter 1
            index: Positional parameter 2
        """
        return self(f"STRing.CHAR({fmt(string)}, {fmt(index)})", int)

    def string_compare(self, string: str, pattern: str) -> bool:
        """Check if string matches pattern

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1358201>`__.

        Args:
            string: Positional parameter 1
            pattern: Positional parameter 2
        """
        return self(f"STRing.ComPare({fmt(string)}, {fmt(pattern)})", bool)

    def string_count(self, string: str, substring: str) -> int:
        """Substring occurrences

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1422870>`__.

        Args:
            string: Positional parameter 1
            substring: Positional parameter 2
        """
        return self(f"STRing.COUNT({fmt(string)}, {fmt(substring)})", int)

    def string_cut(self, string: str, length: int) -> str:
        """Cut string from left or right

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1630970>`__.

        Args:
            string: Positional parameter 1
            length: Positional parameter 2
        """
        return self(f"STRing.CUT({fmt(string)}, {fmt(length)})", str)

    def string_escapequotes(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"STRing.ESCapeQuotes({fmt(string)})", str)

    def string_find(self, string1: str, string2: str) -> bool:
        """Check if search characters are found within string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1631069>`__.

        Args:
            string1: Positional parameter 1
            string2: Positional parameter 2
        """
        return self(f"STRing.FIND({fmt(string1)}, {fmt(string2)})", bool)

    def string_length(self, string: str) -> int:
        """Length of string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1357445>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"STRing.LENgth({fmt(string)})", int)

    def string_lower(self, string: str) -> str:
        """String to lowercase

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1357280>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"STRing.LoWeR({fmt(string)})", str)

    def string_mid(self, string: str, start_at: int, length: int) -> str:
        """Extract part of string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1357064>`__.

        Args:
            string: Positional parameter 1
            start_at: Positional parameter 2
            length: Positional parameter 3
        """
        return self(f"STRing.MID({fmt(string)}, {fmt(start_at)}, {fmt(length)})", str)

    def string_replace(self, source_string: str, search_string: str, replace_string: str, no_replaces: int) -> str:
        """Modified string after search operation

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1356553>`__.

        Args:
            source_string: Positional parameter 1
            search_string: Positional parameter 2
            replace_string: Positional parameter 3
            no_replaces: Positional parameter 4
        """
        return self(f"STRing.Replace({fmt(source_string)}, {fmt(search_string)}, {fmt(replace_string)}, {fmt(no_replaces)})", str)

    def string_scan(self, source_string: str, search_string: str, start_at: int) -> int:
        """Offset of the found string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1631474>`__.

        Args:
            source_string: Positional parameter 1
            search_string: Positional parameter 2
            start_at: Positional parameter 3
        """
        return self(f"STRing.SCAN({fmt(source_string)}, {fmt(search_string)}, {fmt(start_at)})", int)

    def string_scanandextract(self, string: str, key: str, default_value: str) -> str:
        """Extract remaining string after search string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1433557>`__.

        Args:
            string: Positional parameter 1
            key: Positional parameter 2
            default_value: Positional parameter 3
        """
        return self(f"STRing.SCANAndExtract({fmt(string)}, {fmt(key)}, {fmt(default_value)})", str)

    def string_scanback(self, source_string: str, search_string: str, start_at: int) -> int:
        """Offset of the found string

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1838338>`__.

        Args:
            source_string: Positional parameter 1
            search_string: Positional parameter 2
            start_at: Positional parameter 3
        """
        return self(f"STRing.SCANBack({fmt(source_string)}, {fmt(search_string)}, {fmt(start_at)})", int)

    def string_split(self, string1: str, string2: str, number: int, string3: str) -> str:
        """Return element from string list

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1355984>`__.

        Args:
            string1: Positional parameter 1
            string2: Positional parameter 2
            number: Positional parameter 3
            string3: Positional parameter 4
        """
        return self(f"STRing.SPLIT({fmt(string1)}, {fmt(string2)}, {fmt(number)}, {fmt(string3)})", str)

    def string_token(self, string1: str, string2: str, number: int, string3: str) -> str:
        """
        Args:
            string1: Positional parameter 1
            string2: Positional parameter 2
            number: Positional parameter 3
            string3: Positional parameter 4
        """
        return self(f"STRing.TOKEN({fmt(string1)}, {fmt(string2)}, {fmt(number)}, {fmt(string3)})", str)

    def string_trim(self, string: str) -> str:
        """String without leading and trailing whitespaces

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1355850>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"STRing.TRIM({fmt(string)})", str)

    def string_upper(self, string: str) -> str:
        """String to uppercase

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1355816>`__.

        Args:
            string: Positional parameter 1
        """
        return self(f"STRing.UPpeR({fmt(string)})", str)

    def symbol_attribute(self, address: Address) -> int:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.ATTRIBUTE({fmt(address)})", int)

    def symbol_autoload_check(self) -> str:
        """Update option for the symbol autoloader

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1859858>`__.
        """
        return self("sYmbol.AutoLOAD.CHECK()", str)

    def symbol_autoload_checkcmd(self, number: int) -> str:
        """Load command for symbol autoloader

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1860148>`__.

        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.AutoLOAD.CHECKCMD({fmt(number)})", str)

    def symbol_autoload_config(self, number: int) -> str:
        """Used sub-command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1859625>`__.

        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.AutoLOAD.CONFIG({fmt(number)})", str)

    def symbol_begin(self, symbol: str) -> Address:
        """First address of symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1392564>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.BEGIN({fmt(symbol)})", Address)

    def symbol_count(self, symbol: str) -> int:
        """Number of symbols

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1989432>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.COUNT({fmt(symbol)})", int)

    def symbol_end(self, symbol: str) -> Address:
        """Last address of symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1392818>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.END({fmt(symbol)})", Address)

    def symbol_epilog(self, symbol: str) -> Address:
        """Address of return point

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2024432>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.EPILOG({fmt(symbol)})", Address)

    def symbol_exist(self, symbol: str) -> bool:
        """TRUE if symbol exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1338731>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.EXIST({fmt(symbol)})", bool)

    def symbol_exit(self, symbol: str) -> Address:
        """Exit address of function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1358604>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.EXIT({fmt(symbol)})", Address)

    def symbol_function(self, address: Address) -> str:
        """Function name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1392967>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.FUNCTION({fmt(address)})", str)

    def symbol_import(self) -> str:
        """Import file names

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1392984>`__.
        """
        return self("sYmbol.IMPORT()", str)

    def symbol_isfunction(self, symbol: str) -> bool:
        """TRUE if symbol is function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2932177>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.ISFUNCTION({fmt(symbol)})", bool)

    def symbol_isregister(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"sYmbol.ISREGISTER({fmt(string)})", bool)

    def symbol_isstack(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"sYmbol.ISSTACK({fmt(string)})", bool)

    def symbol_isstatic(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"sYmbol.ISSTATIC({fmt(string)})", bool)

    def symbol_isvariable(self, symbol: str) -> bool:
        """TRUE if symbol is variable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2932268>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.ISVARIABLE({fmt(symbol)})", bool)

    def symbol_language(self) -> str:
        """Selected high-level language

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2799016>`__.
        """
        return self("sYmbol.LANGUAGE()", str)

    def symbol_list_map_begin(self, index: int) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2528988>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"sYmbol.List.MAP.BEGIN({fmt(index)})", Address)

    def symbol_list_map_count(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2528986>`__.
        """
        return self("sYmbol.List.MAP.COUNT()", int)

    def symbol_list_map_end(self, index: int) -> Address:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2528990>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"sYmbol.List.MAP.END({fmt(index)})", Address)

    def symbol_list_map_range(self, index: int) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2528992>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"sYmbol.List.MAP.RANGE({fmt(index)})", AddressRange)

    def symbol_list_program(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.PROGRAM({fmt(number)})", str)

    def symbol_list_program_command(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.Program.COMMAND({fmt(number)})", str)

    def symbol_list_program_count(self) -> int:
        return self("sYmbol.List.Program.COUNT()", int)

    def symbol_list_program_file(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.Program.FILE({fmt(number)})", str)

    def symbol_list_program_format(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.Program.FORMAT({fmt(number)})", str)

    def symbol_list_program_name(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.Program.NAME({fmt(number)})", str)

    def symbol_list_program_range(self, number: int) -> AddressRange:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"sYmbol.List.Program.RANGE({fmt(number)})", AddressRange)

    def symbol_list_section_count(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3076713>`__.
        """
        return self("sYmbol.List.SECtion.COUNT()", int)

    def symbol_list_section_path(self, index: int) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3076715>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"sYmbol.List.SECtion.PATH({fmt(index)})", str)

    def symbol_list_section_range(self, index: int) -> AddressRange:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3076717>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"sYmbol.List.SECtion.RANGE({fmt(index)})", AddressRange)

    def symbol_list_source(self, number1: int, number2: int, number3: int) -> str:
        """
        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
            number3: Positional parameter 3
        """
        return self(f"sYmbol.List.SOURCE({fmt(number1)}, {fmt(number2)}, {fmt(number3)})", str)

    def symbol_loadedbytes(self) -> int:
        return self("sYmbol.LOADEDBYTES()", int)

    def symbol_matches(self) -> int:
        """Number of occurrences

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1393820>`__.
        """
        return self("sYmbol.MATCHES()", int)

    def symbol_name(self, address: Address) -> str:
        """Resolve ambiguous symbols based on address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1393828>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.NAME({fmt(address)})", str)

    def symbol_name_at(self, address: str, context_address: Address) -> str:
        """Resolve ambiguous symbols based on address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1303228>`__.

        Args:
            address: Positional parameter 1
            context_address: Positional parameter 2
        """
        return self(f"sYmbol.NAME.AT({fmt(address)}, {fmt(context_address)})", str)

    def symbol_next_begin(self, symbol: str) -> Address:
        """Start address of next symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394072>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.NEXT.BEGIN({fmt(symbol)})", Address)

    def symbol_range(self, symbol: str) -> AddressRange:
        """Address range of symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394356>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.RANGE({fmt(symbol)})", AddressRange)

    def symbol_register(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"sYmbol.REGISTER({fmt(string)})", str)

    def symbol_searchfile(self, file: str) -> str:
        """Absolute path of source file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1465702>`__.

        Args:
            file: Positional parameter 1
        """
        return self(f"sYmbol.SEARCHFILE({fmt(file)})", str)

    def symbol_secaddress(self, section: str) -> Address:
        """Start address of section

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394190>`__.

        Args:
            section: Positional parameter 1
        """
        return self(f"sYmbol.SECADDRESS({fmt(section)})", Address)

    def symbol_secend(self, section: str) -> Address:
        """End address of section

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394434>`__.

        Args:
            section: Positional parameter 1
        """
        return self(f"sYmbol.SECEND({fmt(section)})", Address)

    def symbol_secexist(self, section: str) -> bool:
        """Check for existence of a section

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2757244>`__.

        Args:
            section: Positional parameter 1
        """
        return self(f"sYmbol.SECEXIST({fmt(section)})", bool)

    def symbol_secname(self, address: Address) -> str:
        """Section name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2524445>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.SECNAME({fmt(address)})", str)

    def symbol_secprange(self, section: str) -> AddressRange:
        """Physical address range of section

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394456>`__.

        Args:
            section: Positional parameter 1
        """
        return self(f"sYmbol.SECPRANGE({fmt(section)})", AddressRange)

    def symbol_secrange(self, section: str) -> AddressRange:
        """Logical address range of section

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1394474>`__.

        Args:
            section: Positional parameter 1
        """
        return self(f"sYmbol.SECRANGE({fmt(section)})", AddressRange)

    def symbol_sizeof(self, symbol: str) -> int:
        """Size of debug symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1465405>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.SIZEOF({fmt(symbol)})", int)

    def symbol_sourcefile(self, address_or_symbol: Address) -> str:
        """Name of source file

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1465280>`__.

        Args:
            address_or_symbol: Positional parameter 1
        """
        return self(f"sYmbol.SOURCEFILE({fmt(address_or_symbol)})", str)

    def symbol_sourceline(self, address: Address) -> int:
        """HLL-line number of address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1464874>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.SOURCELINE({fmt(address)})", int)

    def symbol_sourcepath(self, directory_path: str) -> bool:
        """TRUE if path is search path

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1464998>`__.

        Args:
            directory_path: Positional parameter 1
        """
        return self(f"sYmbol.SOURCEPATH({fmt(directory_path)})", bool)

    def symbol_state(self, name: str) -> str:
        """Value from sYmbol.state window

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1464475>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"sYmbol.STATE({fmt(name)})", str)

    def symbol_transpose(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"sYmbol.TRANSPOSE({fmt(string)})", str)

    def symbol_type(self, symbol: str) -> int:
        """Type of symbol

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1464646>`__.

        Args:
            symbol: Positional parameter 1
        """
        return self(f"sYmbol.TYPE({fmt(symbol)})", int)

    def symbol_varname(self, address: Address) -> str:
        """Name of variable or structure element

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1464567>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"sYmbol.VARNAME({fmt(address)})", str)

    def system_access_denied(self) -> bool:
        """TRUE if memory access is denied

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1491962>`__.
        """
        return self("SYStem.ACCESS.DENIED()", bool)

    def system_adapter_fw_outdated(self, number: int) -> bool:
        """Only available for ARM, I386, I386_64.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.ADAPTER.FW.OUTDATED({fmt(number)})", bool)

    def system_amba(self) -> bool:
        """TRUE if AMBA bus mode is selected

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2762471>`__.

        Only available for ARM.
        """
        return self("SYStem.AMBA()", bool)

    def system_baudrate(self) -> str:
        """Only available for V800.
        """
        return self("SYStem.BAUDRATE()", str)

    def system_bigendian(self) -> bool:
        """TRUE if target core runs in big endian mode

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2762431>`__.
        """
        return self("SYStem.BigEndian()", bool)

    def system_cadiconfig_remoteserver(self, key: int) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2600899>`__.

        Only available for ARM.

        Args:
            key: Positional parameter 1
        """
        return self(f"SYStem.CADIconfig.RemoteServer({fmt(key)})", str)

    def system_cadiconfig_traceconfig(self, value: int) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2600946>`__.

        Only available for ARM.

        Args:
            value: Positional parameter 1
        """
        return self(f"SYStem.CADIconfig.Traceconfig({fmt(value)})", str)

    def system_cfid(self, number: int) -> int:
        """Only available for V800.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.CFID({fmt(number)})", int)

    def system_config_debugport(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1491638>`__.
        """
        return self("SYStem.CONFIG.DEBUGPORT()", str)

    def system_config_debugporttype(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1491510>`__.
        """
        return self("SYStem.CONFIG.DEBUGPORTTYPE()", str)

    def system_config_drpost(self, core_index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542686>`__.

        Args:
            core_index: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.DRPOST({fmt(core_index)})", int)

    def system_config_drpre(self, core_index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542688>`__.

        Args:
            core_index: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.DRPRE({fmt(core_index)})", int)

    def system_config_irpost(self, core_index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542690>`__.

        Args:
            core_index: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.IRPOST({fmt(core_index)})", int)

    def system_config_irpre(self, core_index: int) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542679>`__.

        Args:
            core_index: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.IRPRE({fmt(core_index)})", int)

    def system_config_jtagtap(self, item: str, config_index: int) -> int:
        """Return the JTAG PRE and POST settings

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2580470>`__.

        Args:
            item: Positional parameter 1
            config_index: Positional parameter 2
        """
        return self(f"SYStem.CONFIG.JTAGTAP({fmt(item)}, {fmt(config_index)})", int)

    def system_config_listcore(self, line_number: int, column_string: str) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1305870>`__.

        Only available for ARC, ARM, CEVAX, CUSTOM64, GTM, I386, I386_64, I51, IPU, OAK, PCP, POWERPC, POWERPC64, QDSP6, RISCV, SPT, TRICORE, UBICOM32, V800, XTENSA.

        Args:
            line_number: Positional parameter 1
            column_string: Positional parameter 2
        """
        return self(f"SYStem.CONFIG.ListCORE({fmt(line_number)}, {fmt(column_string)})", str)

    def system_config_listsim(self, line_number: int, column_string: str) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1306043>`__.

        Only available for ARC, ARM, CEVAX, CUSTOM64, GTM, I386, I386_64, I51, IPU, OAK, PCP, POWERPC, POWERPC64, QDSP6, RISCV, SPT, TRICORE, UBICOM32, V800, XTENSA.

        Args:
            line_number: Positional parameter 1
            column_string: Positional parameter 2
        """
        return self(f"SYStem.CONFIG.ListSIM({fmt(line_number)}, {fmt(column_string)})", str)

    def system_config_pch(self) -> str:
        """Only available for I386, I386_64.
        """
        return self("SYStem.CONFIG.PCH()", str)

    def system_config_slave(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542844>`__.
        """
        return self("SYStem.CONFIG.Slave()", bool)

    def system_config_swdp(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C2000, C5000, C6000, C7000_64, CUSTOM64, ETPU, IPU, MICROBLAZE, OAK, PRU, RISCV, SDMA, SPT, STRED, XTENSA.
        """
        return self("SYStem.CONFIG.SWDP()", bool)

    def system_config_swdptargetid(self) -> int:
        """Only available for APEX, ARC, ARM, ARP32, C2000, C5000, C6000, C7000_64, CUSTOM64, ETPU, IPU, MICROBLAZE, OAK, PRU, RISCV, SDMA, SPT, STRED, XTENSA.
        """
        return self("SYStem.CONFIG.SWDPTargetId()", int)

    def system_config_swdptargetsel(self) -> int:
        """Only available for APEX, ARC, ARM, ARP32, C2000, C5000, C6000, C7000_64, CUSTOM64, ETPU, IPU, MICROBLAZE, OAK, PRU, RISCV, SDMA, SPT, STRED, XTENSA.
        """
        return self("SYStem.CONFIG.SWDPTargetSel()", int)

    def system_config_tapstate(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1913576>`__.
        """
        return self("SYStem.CONFIG.TAPState()", int)

    def system_config_xcp_connected(self) -> bool:
        """Current XCP connection state

        See `XCP Debug Back-End <https://www.lauterbach.com/pdf/backend_xcp.pdf#G1153081>`__.

        Only available for ARC, ARM, I51, POWERPC, TRICORE, V800.
        """
        return self("SYStem.CONFIG.XCP.Connected()", bool)

    def system_config_xcp_connectmode(self) -> str:
        """XCP connection mode

        See `XCP Debug Back-End <https://www.lauterbach.com/pdf/backend_xcp.pdf#G1152942>`__.

        Only available for ARC, ARM, I51, POWERPC, TRICORE, V800.
        """
        return self("SYStem.CONFIG.XCP.ConnectMode()", str)

    def system_config_xcp_info(self, property: str) -> int:
        """String value of slave property

        See `XCP Debug Back-End <https://www.lauterbach.com/pdf/backend_xcp.pdf#G1152495>`__.

        Only available for ARC, ARM, I51, POWERPC, TRICORE, V800.

        Args:
            property: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.XCP.INFO({fmt(property)})", int)

    def system_config_xcp_info_str(self, property: str) -> str:
        """String value of slave property

        See `XCP Debug Back-End <https://www.lauterbach.com/pdf/backend_xcp.pdf#G1141954>`__.

        Only available for ARC, ARM, I51, POWERPC, TRICORE, V800.

        Args:
            property: Positional parameter 1
        """
        return self(f"SYStem.CONFIG.XCP.INFO.STR({fmt(property)})", str)

    def system_coreclock(self) -> int:
        """Only available for V800.
        """
        return self("SYStem.CORECLOCK()", int)

    def system_corestates_apic(self, core: int) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2248173>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.APIC({fmt(core)})", int)

    def system_corestates_hyper(self, core: int) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2248416>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.HYPER({fmt(core)})", int)

    def system_corestates_mode(self, core: int) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2248623>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.MODE({fmt(core)})", str)

    def system_corestates_phys(self, core: int) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2248827>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.PHYS({fmt(core)})", int)

    def system_corestates_prior(self, core: int) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249031>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.PRIOR({fmt(core)})", str)

    def system_corestates_smm(self, core: int) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249232>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.SMM({fmt(core)})", str)

    def system_corestates_vmx(self, core: int) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249429>`__.

        Only available for I386, I386_64.

        Args:
            core: Positional parameter 1
        """
        return self(f"SYStem.CoreStates.VMX({fmt(core)})", str)

    def system_cpu(self) -> str:
        """Name of processor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1913565>`__.
        """
        return self("SYStem.CPU()", str)

    def system_dcfreeze(self) -> bool:
        """Only available for POWERPC, POWERPC64.
        """
        return self("SYStem.DCFreeze()", bool)

    def system_dci_bridge(self) -> str:
        """Currently selected DCI bridge

        See `Debugging via Intel(r) DCI User's Guide <https://www.lauterbach.com/pdf/dci_intel_user.pdf#G1165462>`__.

        Only available for ARC, I386, I386_64, I51, XTENSA.
        """
        return self("SYStem.DCI.Bridge()", str)

    def system_dci_bssbclock(self, clock_name: str) -> int:
        """Currently selected DCI OOB clock

        See `Debugging via Intel(r) DCI User's Guide <https://www.lauterbach.com/pdf/dci_intel_user.pdf#G1165487>`__.

        Only available for ARC, I386, I386_64, I51, XTENSA.

        Args:
            clock_name: Positional parameter 1
        """
        return self(f"SYStem.DCI.BssbClock({fmt(clock_name)})", int)

    def system_dci_timeout(self, string: str) -> float:
        """Only available for ARC, I386, I386_64, I51, XTENSA.

        Args:
            string: Positional parameter 1
        """
        return self(f"SYStem.DCI.TimeOut({fmt(string)})", float)

    def system_detect_cltapchain(self) -> str:
        """Only available for I386, I386_64.
        """
        return self("SYStem.DETECT.CLTapchain()", str)

    def system_detect_stepping(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("SYStem.DETECT.STEPping()", int)

    def system_dfid(self, number: int) -> int:
        """Only available for V800.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.DFID({fmt(number)})", int)

    def system_gtl_callcounter(self) -> int:
        return self("SYStem.GTL.CALLCOUNTER()", int)

    def system_gtl_connected(self) -> bool:
        """Connection status

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2575430>`__.
        """
        return self("SYStem.GTL.CONNECTED()", bool)

    def system_gtl_libname(self) -> str:
        """Name of GTL library

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1643243>`__.
        """
        return self("SYStem.GTL.LIBname()", str)

    def system_gtl_modelinfo(self, n: int) -> str:
        """Info string from GTL API

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3035785>`__.

        Args:
            n: Positional parameter 1
        """
        return self(f"SYStem.GTL.ModelINFO({fmt(n)})", str)

    def system_gtl_modelname(self, index: int) -> str:
        """Model Name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3035874>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"SYStem.GTL.ModelNAME({fmt(index)})", str)

    def system_gtl_pluginversion(self) -> int:
        """Version number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1643254>`__.
        """
        return self("SYStem.GTL.PLUGINVERSION()", int)

    def system_gtl_transactorname(self, index: int) -> str:
        """Transactor name

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3035913>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"SYStem.GTL.TransactorNAME({fmt(index)})", str)

    def system_gtl_transactortype(self, index: int) -> str:
        """Transactor type

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3035933>`__.

        Args:
            index: Positional parameter 1
        """
        return self(f"SYStem.GTL.TransactorTYPE({fmt(index)})", str)

    def system_gtl_vendorid(self) -> str:
        """Vendor ID

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1643264>`__.
        """
        return self("SYStem.GTL.VENDORID()", str)

    def system_gtl_version(self) -> int:
        """Version number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1643274>`__.
        """
        return self("SYStem.GTL.VERSION()", int)

    def system_hook(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1638589>`__.

        Only available for POWERPC, POWERPC64.
        """
        return self("SYStem.HOOK()", int)

    def system_imaskasm(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1489947>`__.
        """
        return self("SYStem.IMASKASM()", bool)

    def system_imaskhll(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1766419>`__.
        """
        return self("SYStem.IMASKHLL()", bool)

    def system_instance(self) -> int:
        """Index of TRACE32 PowerView instance

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2567762>`__.
        """
        return self("SYStem.INSTANCE()", int)

    def system_instancecount(self) -> int:
        """Count of GUIs connected to a PowerDebug

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2725392>`__.
        """
        return self("SYStem.INSTANCECOUNT()", int)

    def system_irisconfig_remoteserver(self, key: int) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2725374>`__.

        Only available for ARM.

        Args:
            key: Positional parameter 1
        """
        return self(f"SYStem.IRISconfig.RemoteServer({fmt(key)})", str)

    def system_jtagclock(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1489810>`__.
        """
        return self("SYStem.JtagClock()", int)

    def system_jtagclock_whisker(self, string: str) -> int:
        """Only available for I386, I386_64.

        Args:
            string: Positional parameter 1
        """
        return self(f"SYStem.JtagClock.Whisker({fmt(string)})", int)

    def system_littleendian(self) -> bool:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1489733>`__.
        """
        return self("SYStem.LittleEndian()", bool)

    def system_mcdcommand_resultstring(self) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2975323>`__.

        Only available for ARC, ARM, CEVAX, CUSTOM64, GTM, I386, I386_64, I51, IPU, OAK, PCP, POWERPC, POWERPC64, QDSP6, RISCV, SPT, TRICORE, UBICOM32, V800, XTENSA.
        """
        return self("SYStem.MCDCommand.ResultString()", str)

    def system_mcdconfig_library(self, key: int) -> str:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2022812>`__.

        Only available for ARC, ARM, CEVAX, CUSTOM64, GTM, I386, I386_64, I51, IPU, OAK, PCP, POWERPC, POWERPC64, QDSP6, RISCV, SPT, TRICORE, UBICOM32, V800, XTENSA.

        Args:
            key: Positional parameter 1
        """
        return self(f"SYStem.MCDconfig.LIBrary({fmt(key)})", str)

    def system_memaccess(self) -> str:
        return self("SYStem.MEMACCESS()", str)

    def system_mmu(self) -> bool:
        """Only available for ANDES, ARC, ARM, BEYOND, C7000_64, I386, I386_64, M68K, MICROBLAZE, MIPS, MIPS64, NIOS, POWERPC, POWERPC64, QDSP6, RISCV, SC100, SH, XTENSA.
        """
        return self("SYStem.MMU()", bool)

    def system_mode(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2022805>`__.
        """
        return self("SYStem.Mode()", int)

    def system_notrap(self) -> int:
        """1 if the option NOTRAP is active

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1489420>`__.

        Only available for POWERPC, POWERPC64.
        """
        return self("SYStem.NOTRAP()", int)

    def system_ocdid(self, number: int) -> int:
        """Only available for V800.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.OCDID({fmt(number)})", int)

    def system_opbt(self, number: int) -> int:
        """Only available for V800.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.OPBT({fmt(number)})", int)

    def system_opbt8(self, number: int) -> int:
        """Only available for V800.

        Args:
            number: Positional parameter 1
        """
        return self(f"SYStem.OPBT8({fmt(number)})", int)

    def system_option_cmnread(self, number1: int, number2: int, number3: int) -> int:
        """Only available for I386, I386_64.

        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
            number3: Positional parameter 3
        """
        return self(f"SYStem.Option.CMNREAD({fmt(number1)}, {fmt(number2)}, {fmt(number3)})", int)

    def system_option_dualport(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2688712>`__.

        Only available for ARM, C166, C5000, C6000, C7000_64, ETPU, GTM, MCORE, MICO32, MICROBLAZE, PCP, POWERPC, POWERPC64, SDMA, TRICORE, V800.
        """
        return self("SYStem.Option.DUALPORT()", bool)

    def system_option_enreset(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2858638>`__.

        Only available for ARM.
        """
        return self("SYStem.Option.EnReset()", bool)

    def system_option_fastaccess(self) -> bool:
        """Only available for POWERPC, POWERPC64.
        """
        return self("SYStem.Option.FASTACCESS()", bool)

    def system_option_machinespaces(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2596382>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, TRICORE, V800.
        """
        return self("SYStem.Option.MACHINESPACES()", bool)

    def system_option_memorymodel(self) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249623>`__.

        Only available for I386, I386_64.
        """
        return self("SYStem.Option.MEMoryMODEL()", str)

    def system_option_mmuspaces(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2596940>`__.

        Only available for ANDES, ARC, ARM, BEYOND, C7000_64, I386, I386_64, M68K, MICROBLAZE, MIPS, MIPS64, NIOS, POWERPC, POWERPC64, QDSP6, RISCV, SC100, SH, XTENSA.
        """
        return self("SYStem.Option.MMUSPACES()", bool)

    def system_option_partitionconfig(self) -> int:
        """Only available for PIC.
        """
        return self("SYStem.Option.PARTitionconfig()", int)

    def system_option_resbreak(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2936919>`__.

        Only available for ARM.
        """
        return self("SYStem.Option.ResBreak()", bool)

    def system_option_spilllocation(self) -> int:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G3038328>`__.

        Only available for XTENSA.
        """
        return self("SYStem.Option.SPILLLOCation()", int)

    def system_option_swdcontrolstatus(self) -> int:
        """Only available for I386, I386_64.
        """
        return self("SYStem.Option.SWDCONTROLSTATUS()", int)

    def system_option_swdread(self, number1: int, number2: int) -> int:
        """Only available for I386, I386_64.

        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
        """
        return self(f"SYStem.Option.SWDREAD({fmt(number1)}, {fmt(number2)})", int)

    def system_option_topology(self) -> str:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2699253>`__.

        Only available for I386, I386_64.
        """
        return self("SYStem.Option.TOPOlogy()", str)

    def system_option_topology_sockets(self) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2699346>`__.

        Only available for I386, I386_64.
        """
        return self("SYStem.Option.TOPOlogy.SOCKETS()", int)

    def system_option_zonespaces(self) -> bool:
        """State of like-named command

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2596278>`__.

        Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, RISCV.
        """
        return self("SYStem.Option.ZoneSPACES()", bool)

    def system_oscclock(self) -> int:
        """Only available for V800.
        """
        return self("SYStem.OSCCLOCK()", int)

    def system_pch(self) -> str:
        """Only available for I386, I386_64.
        """
        return self("SYStem.PCH()", str)

    def system_readpdrh(self) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249850>`__.

        Only available for I386, I386_64.
        """
        return self("SYStem.ReadPDRH()", int)

    def system_readpdrl(self) -> int:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2249997>`__.

        Only available for I386, I386_64.
        """
        return self("SYStem.ReadPDRL()", int)

    def system_resetbehavior(self) -> str:
        """Current setting of RESetBehavior

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487954>`__.

        Only available for TRICORE, V800.
        """
        return self("SYStem.RESetBehavior()", str)

    def system_resetdetection(self) -> str:
        """Only available for V800.
        """
        return self("SYStem.RESETDETECTION()", str)

    def system_traceext(self) -> bool:
        """TRUE if an external trace is activated

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487884>`__.
        """
        return self("SYStem.TRACEEXT()", bool)

    def system_traceint(self) -> bool:
        """TRUE if an internal trace is activated

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487815>`__.
        """
        return self("SYStem.TRACEINT()", bool)

    def system_up(self) -> bool:
        """TRUE if debugger has access to debug resources

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487652>`__.
        """
        return self("SYStem.Up()", bool)

    def system_up_islocked(self) -> bool:
        return self("SYStem.Up.isLOCKED()", bool)

    def system_usecore(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487586>`__.
        """
        return self("SYStem.USECORE()", int)

    def system_usemask(self) -> int:
        """See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1487415>`__.
        """
        return self("SYStem.USEMASK()", int)

    def task(self) -> str:
        """Name of current task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1671803>`__.
        """
        return self("TASK()", str)

    def task_access(self) -> str:
        """Access class

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2789885>`__.
        """
        return self("TASK.ACCESS()", str)

    def task_access_zone(self) -> str:
        """Access class zone

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2789902>`__.
        """
        return self("TASK.ACCESS.ZONE()", str)

    def task_back(self) -> int:
        """Background task number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1493733>`__.
        """
        return self("TASK.BACK()", int)

    def task_configfile(self) -> str:
        """Path of loaded OS Awareness

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2062165>`__.
        """
        return self("TASK.CONFIGFILE()", str)

    def task_count(self) -> int:
        """Number of tasks

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790469>`__.
        """
        return self("TASK.COUNT()", int)

    def task_current_machineid(self) -> int:
        """ID of current machine

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2978649>`__.
        """
        return self("TASK.CURRENT.MACHINEID()", int)

    def task_current_spaceid(self) -> int:
        """ID of current MMU space

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2978512>`__.
        """
        return self("TASK.CURRENT.SPACEID()", int)

    def task_current_task(self) -> int:
        """Magic value of current task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2978443>`__.
        """
        return self("TASK.CURRENT.TASK()", int)

    def task_current_taskname(self) -> str:
        """Name of current task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2978313>`__.
        """
        return self("TASK.CURRENT.TASKNAME()", str)

    def task_extname(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TASK.EXTNAME({fmt(number)})", str)

    def task_first(self) -> int:
        """First task in list

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790625>`__.
        """
        return self("TASK.FIRST()", int)

    def task_fore(self) -> int:
        """Foreground task number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1493365>`__.
        """
        return self("TASK.FORE()", int)

    def task_id(self, task_name: str) -> int:
        """ID of task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1672001>`__.

        Args:
            task_name: Positional parameter 1
        """
        return self(f"TASK.ID({fmt(task_name)})", int)

    def task_machine_access(self, machine_id: int) -> str:
        """Default access class

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2479955>`__.

        Args:
            machine_id: Positional parameter 1
        """
        return self(f"TASK.MACHINE.ACCESS({fmt(machine_id)})", str)

    def task_machine_extname(self, number1: int, number2: int) -> str:
        """
        Args:
            number1: Positional parameter 1
            number2: Positional parameter 2
        """
        return self(f"TASK.MACHINE.EXTNAME({fmt(number1)}, {fmt(number2)})", str)

    def task_machine_id(self, machine_name: str) -> int:
        """ID of machine

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2789474>`__.

        Args:
            machine_name: Positional parameter 1
        """
        return self(f"TASK.MACHINE.ID({fmt(machine_name)})", int)

    def task_machine_name(self, machine_id_or_machine_magic: int) -> str:
        """Name of machine

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2486910>`__.

        Args:
            machine_id_or_machine_magic: Positional parameter 1
        """
        return self(f"TASK.MACHINE.NAME({fmt(machine_id_or_machine_magic)})", str)

    def task_machine_vttb(self, machine_id_or_machine_magic: int) -> int:
        """VTTB of machine

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2789712>`__.

        Args:
            machine_id_or_machine_magic: Positional parameter 1
        """
        return self(f"TASK.MACHINE.VTTB({fmt(machine_id_or_machine_magic)})", int)

    def task_machineid(self, string: str) -> int:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"TASK.MACHINEID({fmt(string)})", int)

    def task_magic(self, task_name: str) -> int:
        """Task magic number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2789702>`__.

        Args:
            task_name: Positional parameter 1
        """
        return self(f"TASK.MAGIC({fmt(task_name)})", int)

    def task_magicaddress(self) -> Address:
        """'magic address'

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790038>`__.
        """
        return self("TASK.MAGICADDRESS()", Address)

    def task_magicrange(self) -> AddressRange:
        """Range of 'magic address'

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790332>`__.
        """
        return self("TASK.MAGICRANGE()", AddressRange)

    def task_magicsize(self) -> int:
        """Size of 'magic address'

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790227>`__.
        """
        return self("TASK.MAGICSIZE()", int)

    def task_name(self, task_magic: int) -> str:
        """Name of task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1672028>`__.

        Args:
            task_magic: Positional parameter 1
        """
        return self(f"TASK.NAME({fmt(task_magic)})", str)

    def task_next(self, task_magic: int) -> int:
        """Next task in list

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790735>`__.

        Args:
            task_magic: Positional parameter 1
        """
        return self(f"TASK.NEXT({fmt(task_magic)})", int)

    def task_ortifile(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TASK.ORTIFILE({fmt(number)})", str)

    def task_space_count(self) -> int:
        """Number of spaces

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2790538>`__.
        """
        return self("TASK.SPACE.COUNT()", int)

    def task_spaceid(self, task_name: str) -> int:
        """Space ID of task

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1671946>`__.

        Args:
            task_name: Positional parameter 1
        """
        return self(f"TASK.SPACEID({fmt(task_name)})", int)

    def tcf_discovery(self) -> bool:
        """Check if TCF discovery is enabled

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1565877>`__.
        """
        return self("TCF.DISCOVERY()", bool)

    def tcf_port(self) -> int:
        """Port number of TCF interface

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1565781>`__.
        """
        return self("TCF.PORT()", int)

    def term_line(self, channel: str, line_number: int) -> str:
        """Get line from terminal window

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2546142>`__.

        Args:
            channel: Positional parameter 1
            line_number: Positional parameter 2
        """
        return self(f"TERM.LINE({fmt(channel)}, {fmt(line_number)})", str)

    def term_readbusy(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"TERM.READBUSY({fmt(string)})", bool)

    def term_returncode(self, channel: str) -> int:
        """Get returncode from terminal routine

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2546193>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"TERM.RETURNCODE({fmt(channel)})", int)

    def term_triggered(self, channel: str) -> bool:
        """Get trigger state of terminal window

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2514360>`__.

        Args:
            channel: Positional parameter 1
        """
        return self(f"TERM.TRIGGERED({fmt(channel)})", bool)

    def time_zero(self) -> float:
        return self("TIME.ZERO()", float)

    def timeout(self) -> bool:
        """Check if command was fully executed

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1632478>`__.
        """
        return self("TIMEOUT()", bool)

    def title(self) -> str:
        """Caption of the TRACE32 main window

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1344158>`__.
        """
        return self("TITLE()", str)

    def tpiu_portmode(self) -> str:
        """Port mode setting

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1542906>`__.

        Only available for ARM.
        """
        return self("TPIU.PortMode()", str)

    def tpiu_portsize(self) -> str:
        """Port size setting

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1429269>`__.

        Only available for ARM.
        """
        return self("TPIU.PortSize()", str)

    def tpiu_swvprescaler(self) -> int:
        """SWVPrescaler value

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1429933>`__.

        Only available for ARM.
        """
        return self("TPIU.SWVPrescaler()", int)

    def tpiuavailable(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("TPIUAVAILABLE()", bool)

    def tpiubase(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("TPIUBASE()", Address)

    def tpiufunnelavailable(self) -> bool:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("TPIUFUNNELAVAILABLE()", bool)

    def tpiufunnelbase(self) -> Address:
        """Only available for APEX, ARC, ARM, ARP32, C5000, C6000, C7000_64, CEVAX, CUSTOM64, ETPU, GTM, IPU, MICROBLAZE, NIOS, OAK, PRU, QDSP6, RISCV, SDMA, STRED, UBICOM32, XTENSA.
        """
        return self("TPIUFUNNELBASE()", Address)

    def tpu(self, string: str) -> int:
        """Only available for M68HC16, M68K, POWERPC.

        Args:
            string: Positional parameter 1
        """
        return self(f"TPU({fmt(string)})", int)

    def tpu_idle(self) -> bool:
        """Only available for M68HC16, M68K, POWERPC.
        """
        return self("TPU.IDLE()", bool)

    def tpu_long(self, number: int) -> int:
        """Only available for M68HC16, M68K, POWERPC.

        Args:
            number: Positional parameter 1
        """
        return self(f"TPU.Long({fmt(number)})", int)

    def tpu_run(self) -> bool:
        """Only available for M68HC16, M68K, POWERPC.
        """
        return self("TPU.RUN()", bool)

    def tpubase_address(self) -> Address:
        """Address of TPU

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1430818>`__.

        Only available for M68HC16, M68K, POWERPC.
        """
        return self("TPUBASE.ADDRESS()", Address)

    def trace_file(self) -> str:
        return self("Trace.FILE()", str)

    def trace_first(self) -> int:
        """Get record number of first trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2799534>`__.
        """
        return self("Trace.FIRST()", int)

    def trace_flow(self) -> bool:
        """TRUE if trace method is flow trace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1848579>`__.
        """
        return self("Trace.FLOW()", bool)

    def trace_flow_errors(self) -> int:
        """Get number of flow errors / hard errors

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2208535>`__.
        """
        return self("Trace.FLOW.ERRORS()", int)

    def trace_flow_fifofull(self) -> int:
        """Get number of FIFO overflows

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1553256>`__.
        """
        return self("Trace.FLOW.FIFOFULL()", int)

    def trace_load(self) -> str:
        return self("Trace.LOAD()", str)

    def trace_maxsize(self) -> int:
        """Get max. size of trace buffer in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1462013>`__.
        """
        return self("Trace.MAXSIZE()", int)

    def trace_method(self) -> str:
        """Currently configured trace method

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461987>`__.
        """
        return self("Trace.METHOD()", str)

    def trace_method_analyzer(self) -> bool:
        """TRUE if the trace method is Analyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461720>`__.
        """
        return self("Trace.METHOD.Analyzer()", bool)

    def trace_method_art(self) -> bool:
        """TRUE if the trace method is ART

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461841>`__.
        """
        return self("Trace.METHOD.ART()", bool)

    def trace_method_atrace(self) -> bool:
        return self("Trace.METHOD.ATrace()", bool)

    def trace_method_canalyzer(self) -> bool:
        """TRUE if the trace method is CAnalyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461573>`__.
        """
        return self("Trace.METHOD.CAnalyzer()", bool)

    def trace_method_fdx(self) -> bool:
        """TRUE if the trace method is FDX

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1647927>`__.
        """
        return self("Trace.METHOD.FDX()", bool)

    def trace_method_hanalyzer(self) -> bool:
        """TRUE if the trace method is HAnalyzer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461394>`__.
        """
        return self("Trace.METHOD.HAnalyzer()", bool)

    def trace_method_integrator(self) -> bool:
        """TRUE if the trace method uses the Integrator

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461346>`__.
        """
        return self("Trace.METHOD.Integrator()", bool)

    def trace_method_iprobe(self) -> bool:
        """TRUE if the trace method uses the IProbe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461166>`__.
        """
        return self("Trace.METHOD.IProbe()", bool)

    def trace_method_la(self) -> bool:
        """TRUE if the trace method is LA

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461091>`__.
        """
        return self("Trace.METHOD.LA()", bool)

    def trace_method_logger(self) -> bool:
        """TRUE if the trace method is LOGGER

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1461080>`__.
        """
        return self("Trace.METHOD.LOGGER()", bool)

    def trace_method_onchip(self) -> bool:
        """TRUE if the trace method is ONCHIP

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460825>`__.
        """
        return self("Trace.METHOD.ONCHIP()", bool)

    def trace_method_probe(self) -> bool:
        """TRUE if trace method uses the PowerProbe

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460756>`__.
        """
        return self("Trace.METHOD.Probe()", bool)

    def trace_method_snooper(self) -> bool:
        """TRUE if the trace method is SNOOPer

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460672>`__.
        """
        return self("Trace.METHOD.SNOOPer()", bool)

    def trace_record_address(self, record_number: int) -> Address:
        """Get address recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460375>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Trace.RECORD.ADDRESS({fmt(record_number)})", Address)

    def trace_record_data(self, record_number: int) -> int:
        """Get data recorded in trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460579>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Trace.RECORD.DATA({fmt(record_number)})", int)

    def trace_record_offset(self, record_number: int) -> int:
        """Get address in trace record as number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460485>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Trace.RECORD.OFFSET({fmt(record_number)})", int)

    def trace_record_time(self, record_number: int) -> float:
        """Get timestamp of trace record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460253>`__.

        Args:
            record_number: Positional parameter 1
        """
        return self(f"Trace.RECORD.TIME({fmt(record_number)})", float)

    def trace_records(self) -> int:
        """Get number of used trace records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1460269>`__.
        """
        return self("Trace.RECORDS()", int)

    def trace_size(self) -> int:
        """Get current trace buffer size in records

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1458139>`__.
        """
        return self("Trace.SIZE()", int)

    def trace_state(self) -> int:
        """Get state of PowerTrace hardware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1458235>`__.
        """
        return self("Trace.STATE()", int)

    def trace_statistic_count(self, address: Address) -> int:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.Count({fmt(address)})", int)

    def trace_statistic_exist(self, address: Address) -> bool:
        """TRUE if function exists in trace statistics

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2800305>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.EXIST({fmt(address)})", bool)

    def trace_statistic_imax(self, address: Address) -> float:
        """Longest time between function entry and exit

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2801491>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.IMAX({fmt(address)})", float)

    def trace_statistic_imin(self, address: Address) -> float:
        """Shortest time between function entry and exit

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2801807>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.IMIN({fmt(address)})", float)

    def trace_statistic_internal(self, address: Address) -> float:
        """Time spent within the selected function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2802139>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.Internal({fmt(address)})", float)

    def trace_statistic_max(self, address: Address) -> float:
        """Maximum time of selected function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2800821>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.MAX({fmt(address)})", float)

    def trace_statistic_min(self, address: Address) -> float:
        """Minimum time of selected function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2801188>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.MIN({fmt(address)})", float)

    def trace_statistic_total(self, address: Address) -> float:
        """Total time of selected function

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2800342>`__.

        Args:
            address: Positional parameter 1
        """
        return self(f"Trace.STATistic.Total({fmt(address)})", float)

    def trace_stream_overflows(self) -> bool:
        return self("Trace.STREAM.OVERFLOWS()", bool)

    def trace_traceconnect(self) -> str:
        """Name of trace sink of the SoC

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2172024>`__.
        """
        return self("Trace.TraceCONNECT()", str)

    def traceport_lanecount(self, index: int) -> int:
        """Number of serial lanes

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2613644>`__.

        Only available for ARC, ARM, C6000, CEVAX, ETPU, GTM, POWERPC, POWERPC64, RISCV, TRICORE, V800, XTENSA.

        Args:
            index: Positional parameter 1
        """
        return self(f"TRACEPORT.LaneCount({fmt(index)})", int)

    def track_address(self) -> Address:
        """Get tracking address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456944>`__.
        """
        return self("TRACK.ADDRESS()", Address)

    def track_address_data(self) -> Address:
        return self("TRACK.ADDRESS.DATA()", Address)

    def track_address_prog(self) -> Address:
        return self("TRACK.ADDRESS.PROG()", Address)

    def track_column(self) -> int:
        """Number of column where the found item starts

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456734>`__.
        """
        return self("TRACK.COLUMN()", int)

    def track_line(self) -> int:
        """Number of line containing the found item

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456765>`__.
        """
        return self("TRACK.LINE()", int)

    def track_record(self) -> int:
        """Number of record containing the found item

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456637>`__.
        """
        return self("TRACK.RECORD()", int)

    def track_string(self) -> str:
        """Current selection in a TRACE32 window

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456563>`__.
        """
        return self("TRACK.STRing()", str)

    def track_time(self) -> float:
        """Timestamp of current tracking record

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1456463>`__.
        """
        return self("TRACK.TIME()", float)

    def translation_enable(self) -> bool:
        return self("TRANSlation.ENABLE()", bool)

    def translation_intermediate(self, address: Address) -> Address:
        """Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.INTERMEDIATE({fmt(address)})", Address)

    def translation_intermediate_valid(self, address: Address) -> bool:
        """Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.INTERMEDIATE.VALID({fmt(address)})", bool)

    def translation_intermediateex(self, address: Address) -> Address:
        """Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.INTERMEDIATEEX({fmt(address)})", Address)

    def translation_intermediateex_valid(self, address: Address) -> bool:
        """Only available for ARM, I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.INTERMEDIATEEX.VALID({fmt(address)})", bool)

    def translation_linear(self, address: Address) -> Address:
        """Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LINEAR({fmt(address)})", Address)

    def translation_linear_valid(self, address: Address) -> bool:
        """Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LINEAR.VALID({fmt(address)})", bool)

    def translation_linearex(self, address: Address) -> Address:
        """Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LINEAREX({fmt(address)})", Address)

    def translation_linearex_valid(self, address: Address) -> bool:
        """Only available for I386, I386_64.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LINEAREX.VALID({fmt(address)})", bool)

    def translation_list_logrange(self, number: int) -> AddressRange:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TRANSlation.LIST.LOGRANGE({fmt(number)})", AddressRange)

    def translation_list_logrange_zone(self, number: int, address: Address) -> AddressRange:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"TRANSlation.LIST.LOGRANGE.ZONE({fmt(number)}, {fmt(address)})", AddressRange)

    def translation_list_number(self) -> int:
        return self("TRANSlation.LIST.NUMBER()", int)

    def translation_list_number_zone(self, address: Address) -> int:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LIST.NUMBER.ZONE({fmt(address)})", int)

    def translation_list_physaddr(self, number: int) -> Address:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TRANSlation.LIST.PHYSADDR({fmt(number)})", Address)

    def translation_list_physaddr_zone(self, number: int, address: Address) -> Address:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"TRANSlation.LIST.PHYSADDR.ZONE({fmt(number)}, {fmt(address)})", Address)

    def translation_list_type(self, number: int) -> str:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TRANSlation.LIST.TYPE({fmt(number)})", str)

    def translation_list_type_zone(self, number: int, address: Address) -> str:
        """Only available for ARM, C7000_64, I386, I386_64, POWERPC, POWERPC64, QDSP6, RISCV, TRICORE, V800.

        Args:
            number: Positional parameter 1
            address: Positional parameter 2
        """
        return self(f"TRANSlation.LIST.TYPE.ZONE({fmt(number)}, {fmt(address)})", str)

    def translation_logical(self, address: Address) -> Address:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LOGICAL({fmt(address)})", Address)

    def translation_logical_valid(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.LOGICAL.VALID({fmt(address)})", bool)

    def translation_physical(self, address: Address) -> Address:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.PHYSICAL({fmt(address)})", Address)

    def translation_physical_valid(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.PHYSICAL.VALID({fmt(address)})", bool)

    def translation_physicalex(self, address: Address) -> Address:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.PHYSICALEX({fmt(address)})", Address)

    def translation_physicalex_valid(self, address: Address) -> bool:
        """
        Args:
            address: Positional parameter 1
        """
        return self(f"TRANSlation.PHYSICALEX.VALID({fmt(address)})", bool)

    def translation_tablewalk(self) -> bool:
        return self("TRANSlation.TABLEWALK()", bool)

    def trigger_offset(self) -> int:
        return self("TRIGGER.OFFSET()", int)

    def trims08fll(self, frequency_in_KHz: int) -> int:
        """See `MCS08 Debugger <https://www.lauterbach.com/pdf/debugger_hc08.pdf#G1099661>`__.

        Only available for M68HC08.

        Args:
            frequency_in_KHz: Positional parameter 1
        """
        return self(f"TRIMS08FLL({fmt(frequency_in_KHz)})", int)

    def tronchip_counter(self, number: int) -> int:
        """
        Args:
            number: Positional parameter 1
        """
        return self(f"TrOnchip.COUNTER({fmt(number)})", int)

    def tronchip_isavailable(self, trigger_name: str) -> bool:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2305957>`__.

        Only available for I386, I386_64.

        Args:
            trigger_name: Positional parameter 1
        """
        return self(f"TrOnchip.IsAvailable({fmt(trigger_name)})", bool)

    def tronchip_isset(self, trigger_name: str) -> bool:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2305986>`__.

        Only available for I386, I386_64.

        Args:
            trigger_name: Positional parameter 1
        """
        return self(f"TrOnchip.IsSet({fmt(trigger_name)})", bool)

    def true(self) -> bool:
        """Boolean expression

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342681>`__.
        """
        return self("TRUE()", bool)

    def tss(self) -> int:
        """TSS base address

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1448609>`__.

        Only available for I386, I386_64.
        """
        return self("TSS()", int)

    def var_address(self, hll_expression: str) -> Address:
        """Address of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1453608>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.ADDRESS({fmt(hll_expression)})", Address)

    def var_bitpos(self, hll_expression: str) -> int:
        """Bit position inside a C bit field

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2076596>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.BITPOS({fmt(hll_expression)})", int)

    def var_bitsize(self, hll_expression: str) -> int:
        """Size of bit field element

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1453401>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.BITSIZE({fmt(hll_expression)})", int)

    def var_end(self, hll_expression: str) -> Address:
        """Last address of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2511561>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.END({fmt(hll_expression)})", Address)

    def var_exist(self, hll_expression: str) -> bool:
        """TRUE if HLL expression exists

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2511578>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.EXIST({fmt(hll_expression)})", bool)

    def var_fvalue(self, hll_expression: str) -> float:
        """Contents of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1453170>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.FVALUE({fmt(hll_expression)})", float)

    def var_isbit(self, hll_expression: str) -> bool:
        """TRUE if HLL expression is a bit field element

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1453075>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.ISBIT({fmt(hll_expression)})", bool)

    def var_isregister(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Var.ISREGISTER({fmt(string)})", bool)

    def var_isstack(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Var.ISSTACK({fmt(string)})", bool)

    def var_isstatic(self, string: str) -> bool:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Var.ISSTATIC({fmt(string)})", bool)

    def var_range(self, hll_expression: str) -> AddressRange:
        """Address range of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1452962>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.RANGE({fmt(hll_expression)})", AddressRange)

    def var_register(self, string: str) -> str:
        """
        Args:
            string: Positional parameter 1
        """
        return self(f"Var.REGISTER({fmt(string)})", str)

    def var_sizeof(self, hll_expression: str) -> int:
        """Size of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1452854>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.SIZEOF({fmt(hll_expression)})", int)

    def var_string(self, hll_expression: str) -> str:
        """Zero-terminated string or variable contents

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1452586>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.STRing({fmt(hll_expression)})", str)

    def var_typeof(self, hll_expression: str) -> str:
        """Type of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1198912>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.TYPEOF({fmt(hll_expression)})", str)

    def var_value(self, hll_expression: str) -> int:
        """Value of HLL expression

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1448450>`__.

        Args:
            hll_expression: Positional parameter 1
        """
        return self(f"Var.VALUE({fmt(hll_expression)})", int)

    def vco(self) -> int:
        """Frequency of VCO generator

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1431925>`__.
        """
        return self("VCO()", int)

    def version_build(self) -> int:
        """Upper build number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203141>`__.
        """
        return self("VERSION.BUILD()", int)

    def version_build_base(self) -> int:
        """Lower build number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203205>`__.
        """
        return self("VERSION.BUILD.BASE()", int)

    def version_cable(self) -> int:
        """Hardware version of debug cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1431702>`__.
        """
        return self("VERSION.CABLE()", int)

    def version_date(self) -> str:
        """Version date YYYY/MM

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2858025>`__.
        """
        return self("VERSION.DATE()", str)

    def version_environment(self, name: str) -> str:
        """TRACE32 environment setting

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203281>`__.

        Args:
            name: Positional parameter 1
        """
        return self(f"VERSION.ENVironment({fmt(name)})", str)

    def version_firmware_debug(self) -> float:
        """Version number of firmware

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1430975>`__.
        """
        return self("VERSION.FirmWare.DEBUG()", float)

    def version_serial(self) -> str:
        """Serial number

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203424>`__.
        """
        return self("VERSION.SERIAL()", str)

    def version_serial_cable(self) -> str:
        """First serial number of debug cable

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203416>`__.
        """
        return self("VERSION.SERIAL.CABLE()", str)

    def version_serial_debug(self) -> str:
        """Serial number of debug module

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1431369>`__.
        """
        return self("VERSION.SERIAL.DEBUG()", str)

    def version_serial_integrator(self) -> str:
        return self("VERSION.SERIAL.Integrator()", str)

    def version_serial_nexusadapter(self) -> str:
        return self("VERSION.SERIAL.NEXUSadapter()", str)

    def version_serial_powerprobe(self) -> str:
        return self("VERSION.SERIAL.POWERPROBE()", str)

    def version_serial_powertraceauxport(self) -> str:
        """S/N of device at PT aux port

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2853295>`__.
        """
        return self("VERSION.SERIAL.POWERTRACEAUXPORT()", str)

    def version_serial_preprocessor(self) -> str:
        """Serial number of preprocessor

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1431261>`__.
        """
        return self("VERSION.SERIAL.PREPROcessor()", str)

    def version_serial_trace(self) -> str:
        """Serial number of trace module

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1431115>`__.
        """
        return self("VERSION.SERIAL.TRACE()", str)

    def version_serial_whisker(self, number: int) -> str:
        """S/N of whiskers at CombiProbe or uTrace

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2854085>`__.

        Args:
            number: Positional parameter 1
        """
        return self(f"VERSION.SERIAL.WHISKER({fmt(number)})", str)

    def version_software(self) -> str:
        """Release build or nightly build, etc.

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G2203466>`__.
        """
        return self("VERSION.SOFTWARE()", str)

    def vmx(self) -> bool:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2250127>`__.

        Only available for I386, I386_64.
        """
        return self("VMX()", bool)

    def vmx_guest(self) -> bool:
        """See `Intel(r) x86/x64 Debugger <https://www.lauterbach.com/pdf/debugger_x86.pdf#G2250293>`__.

        Only available for I386, I386_64.
        """
        return self("VMX.Guest()", bool)

    def vpu(self, register_name: str) -> int:
        """Value of VPU register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1435952>`__.

        Only available for APEX, C7000_64, POWERPC, POWERPC64, RISCV.

        Args:
            register_name: Positional parameter 1
        """
        return self(f"VPU({fmt(register_name)})", int)

    def vpucr(self, register: str) -> int:
        """Value of VRSAVE or VSCR register

        See `General Function Reference <https://www.lauterbach.com/pdf/general_func.pdf#G1201038>`__.

        Only available for POWERPC, POWERPC64.

        Args:
            register: Positional parameter 1
        """
        return self(f"VPUCR({fmt(register)})", int)

    def warnings(self) -> bool:
        """Check if warning occurred during command execution

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342852>`__.
        """
        return self("WARNINGS()", bool)

    def window_command(self, WinTOP_or_window_name: str) -> str:
        """Command string displayed in window

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1574347>`__.

        Args:
            WinTOP_or_window_name: Positional parameter 1
        """
        return self(f"WINdow.COMMAND({fmt(WinTOP_or_window_name)})", str)

    def window_exist(self, window_name: str) -> bool:
        """Check if window name exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1342937>`__.

        Args:
            window_name: Positional parameter 1
        """
        return self(f"WINdow.EXIST({fmt(window_name)})", bool)

    def window_position(self, WinTOP_or_window_name: str, position_item_name: str) -> float:
        """Information on window position and dimension

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1343144>`__.

        Args:
            WinTOP_or_window_name: Positional parameter 1
            position_item_name: Positional parameter 2
        """
        return self(f"WINdow.POSition({fmt(WinTOP_or_window_name)}, {fmt(position_item_name)})", float)

    def winpage_exist(self, page_name: str) -> bool:
        """Check if window page exists

        See `PowerView Function Reference <https://www.lauterbach.com/pdf/ide_func.pdf#G1343564>`__.

        Args:
            page_name: Positional parameter 1
        """
        return self(f"WINPAGE.EXIST({fmt(page_name)})", bool)
