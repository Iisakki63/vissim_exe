<?xml version="1.0" encoding="UTF-8"?>
<sc version="202001" id="5" name="" frequency="1" steps="0" defaultIntergreenMatrix="1" interstagesUsingMinDurations="true" checkSum="2096273352">
  <signaldisplays>
    <display id="1" name="Red" state="RED">
      <patterns>
        <pattern pattern="MINUS" color="#FF0000" isBold="true" />
      </patterns>
    </display>
    <display id="2" name="Red/Amber" state="REDAMBER">
      <patterns>
        <pattern pattern="FRAME" color="#CCCC00" isBold="true" />
        <pattern pattern="SLASH" color="#CC0000" isBold="false" />
        <pattern pattern="MINUS" color="#CC0000" isBold="false" />
      </patterns>
    </display>
    <display id="3" name="Green" state="GREEN">
      <patterns>
        <pattern pattern="FRAME" color="#00CC00" isBold="true" />
        <pattern pattern="SOLID" color="#00CC00" isBold="false" />
      </patterns>
    </display>
    <display id="4" name="Amber" state="AMBER">
      <patterns>
        <pattern pattern="FRAME" color="#CCCC00" isBold="true" />
        <pattern pattern="SLASH" color="#CCCC00" isBold="false" />
      </patterns>
    </display>
  </signaldisplays>
  <signalsequences>
    <signalsequence id="3" name="Red-Red/Amber-Green-Amber">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="2" isFixedDuration="true" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="4" isFixedDuration="true" isClosed="true" defaultDuration="3000" />
    </signalsequence>
  </signalsequences>
  <sgs>
    <sg id="1" name="Signal group 1" defaultSignalSequence="3">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="2" duration="1000" />
        <defaultDuration display="3" duration="5000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
    </sg>
    <sg id="2" name="Signal group 2" defaultSignalSequence="3">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="2" duration="1000" />
        <defaultDuration display="3" duration="5000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
    </sg>
    <sg id="3" name="Signal group 3" defaultSignalSequence="3">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="2" duration="1000" />
        <defaultDuration display="3" duration="5000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
    </sg>
  </sgs>
  <dets>
    <det id="1" name="D1" />
    <det id="2" name="D2" />
    <det id="3" name="D3" />
    <det id="4" name="D4" />
    <det id="5" name="D5" />
    <det id="6" name="D6" />
    <det id="7" name="D7" />
    <det id="8" name="D8" />
  </dets>
  <intergreenmatrices>
    <intergreenmatrix id="1" name="Intergreen matrix 1">
      <intergreen clearingsg="2" enteringsg="1" value="3000" />
      <intergreen clearingsg="1" enteringsg="2" value="3000" />
      <intergreen clearingsg="1" enteringsg="3" value="3000" />
      <intergreen clearingsg="2" enteringsg="3" value="3000" />
      <intergreen clearingsg="3" enteringsg="1" value="3000" />
      <intergreen clearingsg="3" enteringsg="2" value="3000" />
    </intergreenmatrix>
  </intergreenmatrices>
  <progs />
  <stages>
    <stage id="1" name="Stage 1" isPseudoStage="false">
      <activations>
        <activation sg_id="1" activation="ON" />
        <activation sg_id="2" activation="OFF" />
        <activation sg_id="3" activation="OFF" />
      </activations>
    </stage>
    <stage id="2" name="Stage 2" isPseudoStage="false">
      <activations>
        <activation sg_id="1" activation="OFF" />
        <activation sg_id="2" activation="ON" />
        <activation sg_id="3" activation="OFF" />
      </activations>
    </stage>
    <stage id="3" name="Stage 3" isPseudoStage="false">
      <activations>
        <activation sg_id="1" activation="OFF" />
        <activation sg_id="2" activation="OFF" />
        <activation sg_id="3" activation="ON" />
      </activations>
    </stage>
  </stages>
  <interstageProgs>
    <interstageProg id="1" cycletime="6000" intergreens="1" fromStage="1" toStage="2" name="1: Stage 1->2: Stage 2">
      <sgs>
        <sg sg_id="1" signal_sequence="3">
          <cmds>
            <cmd display="3" begin="0" />
            <cmd display="1" begin="5000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="2" signal_sequence="3">
          <cmds>
            <cmd display="1" begin="0" />
            <cmd display="3" begin="1000" />
          </cmds>
          <fixedstates>
            <fixedstate display="2" duration="1000" />
          </fixedstates>
        </sg>
        <sg sg_id="3" signal_sequence="1">
          <cmds />
          <fixedstates />
        </sg>
      </sgs>
    </interstageProg>
    <interstageProg id="2" cycletime="6000" intergreens="1" fromStage="2" toStage="3" name="2: Stage 2->3: Stage 3">
      <sgs>
        <sg sg_id="1" signal_sequence="1">
          <cmds />
          <fixedstates />
        </sg>
        <sg sg_id="2" signal_sequence="3">
          <cmds>
            <cmd display="3" begin="0" />
            <cmd display="1" begin="5000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="3" signal_sequence="3">
          <cmds>
            <cmd display="1" begin="0" />
            <cmd display="3" begin="1000" />
          </cmds>
          <fixedstates>
            <fixedstate display="2" duration="1000" />
          </fixedstates>
        </sg>
      </sgs>
    </interstageProg>
    <interstageProg id="3" cycletime="6000" intergreens="1" fromStage="3" toStage="1" name="3: Stage 3->1: Stage 1">
      <sgs>
        <sg sg_id="1" signal_sequence="3">
          <cmds>
            <cmd display="1" begin="0" />
            <cmd display="3" begin="1000" />
          </cmds>
          <fixedstates>
            <fixedstate display="2" duration="1000" />
          </fixedstates>
        </sg>
        <sg sg_id="2" signal_sequence="1">
          <cmds />
          <fixedstates />
        </sg>
        <sg sg_id="3" signal_sequence="3">
          <cmds>
            <cmd display="3" begin="0" />
            <cmd display="1" begin="5000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
      </sgs>
    </interstageProg>
  </interstageProgs>
  <stageProgs>
    <stageProg id="1" cycletime="60000" switchpoint="0" offset="0" intergreens="1" fitness="0.000000" vehicleCount="0" name="Stage 1, Stage 2, Stage 3">
      <interstages>
        <interstage display="1" begin="14000" />
        <interstage display="2" begin="34000" />
        <interstage display="3" begin="54000" />
      </interstages>
    </stageProg>
    <stageProg id="2" cycletime="60000" switchpoint="0" offset="0" intergreens="1" fitness="0.000000" vehicleCount="0" name="Stage 1, Stage 2, Stage 3">
      <interstages>
        <interstage display="1" begin="14000" />
        <interstage display="2" begin="34000" />
        <interstage display="3" begin="54000" />
      </interstages>
    </stageProg>
  </stageProgs>
  <dailyProgLists />
</sc>