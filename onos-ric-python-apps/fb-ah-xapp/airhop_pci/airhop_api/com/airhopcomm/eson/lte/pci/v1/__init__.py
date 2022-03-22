# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: lte_pci.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterator, List, Optional

import betterproto
import grpclib


class Conflict(betterproto.Enum):
    CONFLICT_NONE = 0
    CONFLICT_DIRECT_COLLISION = 1
    CONFLICT_CONFUSION = 2
    CONFLICT_CRS_COLLISION = 3
    CONFLICT_DMRS_COLLISION = 4


@dataclass(eq=False, repr=False)
class SubscribeRequest(betterproto.Message):
    # A set of ECGIs. If ecgi_set is empty, it means all ECGIs.
    ecgi_set: List[int] = betterproto.fixed64_field(1)
    # A set of conflicts. Client will only receive ChangeRequest for conflicts in
    # the set. If conflict_set is empty, it means all conflicts.
    conflict_set: List["Conflict"] = betterproto.enum_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Message(betterproto.Message):
    """PCI service messages."""

    change_req: "ChangeRequest" = betterproto.message_field(1, group="msg")

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ChangeRequest(betterproto.Message):
    """
    PCI change request. This message is sent when the PCI algorithm suggests a
    PCI change.
    """

    ecgi: int = betterproto.fixed64_field(1)
    pci: int = betterproto.uint32_field(2)
    conflict: "Conflict" = betterproto.enum_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AllocateRequest(betterproto.Message):
    # A set of ECGIs. If ecgi_set is empty, it means all ECGIs.
    ecgi_set: List[int] = betterproto.fixed64_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AllocateResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DetectAndResolveRequest(betterproto.Message):
    # A set of ECGIs. If ecgi_set is empty, it means all ECGIs.
    ecgi_set: List[int] = betterproto.fixed64_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DetectAndResolveResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ConfirmChangeRequest(betterproto.Message):
    """The PCI field shall contain the newly proposed PCI."""

    ecgi: int = betterproto.fixed64_field(1)
    pci: int = betterproto.uint32_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ConfirmChangeResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RejectChangeRequest(betterproto.Message):
    """
    The PCI field shall contain the current PCI, not the newly proposed PCI.
    """

    ecgi: int = betterproto.fixed64_field(1)
    pci: int = betterproto.uint32_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RejectChangeResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RetrieveProposedChangesRequest(betterproto.Message):
    # A set of conflicts. Client will only receive ChangeRequest for conflicts in
    # the set. If conflict_set is empty, it means all conflicts.
    conflict_set: List["Conflict"] = betterproto.enum_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RetrieveProposedChangesResponse(betterproto.Message):
    change_reqs: List["ChangeRequest"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


class PciServiceStub(betterproto.ServiceStub):
    """
    The PciService can be used in either autonomous mode or maintenance window
    mode. In autonomous mode, PCI conflicts are detected and changes are
    applied in realtime. The client shall use the Subscribe RPC and monitor the
    return stream for any PCI change. If a PCI change request is received. the
    client shall immediately apply the change. Once the PCI change is applied,
    the client shall use the ConfirmChange or RejectChange RPC to update eSON.
    In maintenance window mode, PCI changes are only applied during the
    maintenance window. The client shall use the RetrieveProposedChanges RPC
    near the end of the maintenance window to obtain a list of suggested PCI
    changes. Once a PCI change is applied, the client shall use the
    ConfirmChange or RejectChange RPC to update eSON. If there are multiple
    clients that subscribe to PCI changes, one and only one shall confirm the
    change.
    """

    async def subscribe(
        self,
        *,
        ecgi_set: Optional[List[int]] = None,
        conflict_set: Optional[List["Conflict"]] = None,
    ) -> AsyncIterator["Message"]:
        """
        Subscribe to the PciService for the PCI algorithm messages. Any future
        PCI change will be streamed back through this RPC.
        """

        ecgi_set = ecgi_set or []
        conflict_set = conflict_set or []

        request = SubscribeRequest()
        request.ecgi_set = ecgi_set
        request.conflict_set = conflict_set

        async for response in self._unary_stream(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/Subscribe", request, Message,
        ):
            yield response

    async def allocate(
        self, *, ecgi_set: Optional[List[int]] = None
    ) -> "AllocateResponse":
        """
        Request initial PCI assignment. The newly allocated PCI is streamed
        back through the Subscribe RPC.
        """

        ecgi_set = ecgi_set or []

        request = AllocateRequest()
        request.ecgi_set = ecgi_set

        return await self._unary_unary(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/Allocate",
            request,
            AllocateResponse,
        )

    async def detect_and_resolve(
        self, *, ecgi_set: Optional[List[int]] = None
    ) -> "DetectAndResolveResponse":
        """
        Trigger PCI algorithm to detect and resolve PCI conflict. If a conflict
        is detected and a better PCI is found, the new PCI is streamed back
        through the Subscribe RPC.
        """

        ecgi_set = ecgi_set or []

        request = DetectAndResolveRequest()
        request.ecgi_set = ecgi_set

        return await self._unary_unary(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/DetectAndResolve",
            request,
            DetectAndResolveResponse,
        )

    async def confirm_change(
        self, *, ecgi: int = 0, pci: int = 0
    ) -> "ConfirmChangeResponse":
        """
        Confirm a PCI change request has been applied. eSON updates its
        internal PCI to reflect the change.
        """

        request = ConfirmChangeRequest()
        request.ecgi = ecgi
        request.pci = pci

        return await self._unary_unary(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/ConfirmChange",
            request,
            ConfirmChangeResponse,
        )

    async def reject_change(
        self, *, ecgi: int = 0, pci: int = 0
    ) -> "RejectChangeResponse":
        """
        Reject a PCI change request if the proposed PCI fails to be applied.
        """

        request = RejectChangeRequest()
        request.ecgi = ecgi
        request.pci = pci

        return await self._unary_unary(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/RejectChange",
            request,
            RejectChangeResponse,
        )

    async def retrieve_proposed_changes(
        self, *, conflict_set: Optional[List["Conflict"]] = None
    ) -> "RetrieveProposedChangesResponse":
        """
        Retrieve a list of proposed PCI changes. The client shall use the
        ConfirmChange or RejectChange later to update the eSON server whether
        the proposed changes are applied. This RPC may take several minutes
        (the current default is 5 minutes) to complete.
        """

        conflict_set = conflict_set or []

        request = RetrieveProposedChangesRequest()
        request.conflict_set = conflict_set

        return await self._unary_unary(
            "/com.airhopcomm.eson.lte.pci.v1.PciService/RetrieveProposedChanges",
            request,
            RetrieveProposedChangesResponse,
        )
