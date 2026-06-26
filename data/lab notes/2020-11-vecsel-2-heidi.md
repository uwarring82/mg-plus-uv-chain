# 2020-11 VECSEL #2 aka Heidi (Photo)

> **Source:** Evernote note exported to ENEX, converted to Markdown.
> **Author:** Ulrich Warring
> **Created:** 2020-11-26 10:04 UTC · **Updated:** 2026-03-19 13:18 UTC
> **Attachments:** 143 files extracted to [`2020-11-vecsel-2-heidi.attachments/`](2020-11-vecsel-2-heidi.attachments/)

---

\[P.K., J.D., U.W.\]\

------------------------------------------------------------------------

Gainchip: **[<u>1140</u>](tel:+491140) <u>nm</u>**\
Case iteration: **<u>V2</u>** (no edge for pump fiber input, enable to mount both types of cooling blocks )\

------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><u>To Dos ()</u><br />
</td>
<td>Short<br />
</td>
<td>More details<br />
</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>Diary:</u>\

------------------------------------------------------------------------

<u>20.07.2022 \[UW\]</u>\

- 8:30h turned on pump, system ran for about 20 min, tried to realign optics to get it lasing again – unsuccessful.\
- 9:20h decided to take out BRF and etalon\
- Lasing near 18 A. For long term test set pump to 30 A and block beam after L1.\

<u>18.07.2022 \[UW\]</u>\

- After several trails, the behaviour is still very puzzling. On-times become shorter....\

![Screenshot 2022-07-20 at 09.16.48.png](2020-11-vecsel-2-heidi.attachments/Screenshot%202022-07-20%20at%2009.16.48.png)<u>13.07.2022 \[UW\]</u>\
![image-5c5fcd.png](2020-11-vecsel-2-heidi.attachments/image-5c5fcd.png)

- <u>9:43h</u> ET temp. still oscillating. PID controller settings:\

<div>

*[controller register dump redacted]*\

</div>

CHANGE to:\

<div>

*[controller register dump redacted]*\

</div>

NOTE: The PID parameters are (and were) not activated in this case. Only the "TEC:GAIN" sets the control loop gain!\

- ET temp continued to oscillate. Changed GAIN setting of controller to 5 (from 10) – helped. Laser fail may not be due to ET. Oscillation may only be a symptom of laser failure. Investigation on-going.\
- GAIN to 3 – there was still small oscillation visible (+/-0.005 °C)\
- 

------------------------------------------------------------------------

<u>12.07.2022 \[UW\]</u>\

- Last few hours look stable:\

|  |  |
|----|----|
| ![Screenshot 2022-07-12 at 08.03.14.png](2020-11-vecsel-2-heidi.attachments/Screenshot%202022-07-12%20at%2008.03.14.png) |  |
|  |  |

- 8:00h Fine-tuning of temperatures to set optical frequency to target value: 262.70290 THz\

![Screenshot 2022-07-12 at 08.07.45.png](2020-11-vecsel-2-heidi.attachments/Screenshot%202022-07-12%20at%2008.07.45.png)

------------------------------------------------------------------------

<u>11.07.2022 \[UW\]</u>\

- I have a look at the system... Pump is off; Serial-to-COM adapter is not working on new pc: no readings and control\

![Screenshot 2022-07-11 at 18.24.32.png](2020-11-vecsel-2-heidi.attachments/Screenshot%202022-07-11%20at%2018.24.32.png)

- 18:30h Etalon set to 30 °C\
  - switch pump on: 28.8 A\
  - power reading near 10 V\
  - wvf meter: 262.69140 THz\
  - etalon warms up to \>40 °C within 1 minute\
- 18:40h ET set to 50°C\
  - et raises above 50°C within few minutes\
- 18:46h ET set to 60°C\
- 19:00h: pump still at 28.8 A, Mon PD still near 10 V, and wavelength at 262.70320 THz\
- ![Screenshot 2022-07-11 at 18.59.17.png](2020-11-vecsel-2-heidi.attachments/Screenshot%202022-07-11%20at%2018.59.17.png)
- lets see...\

------------------------------------------------------------------------

<u>06.07.2022 \[UW\]</u>\

- I was on vacation and DP reported that the system stoped lasing.\
- The etalon temperature regulation show oscillating behavior.\
- First visual inspection of optical elements by JD and DP show no sign of damage\
- System is occasionally lasing – with top lid unscrewed\
- more service next week\

------------------------------------------------------------------------

<u>14.02.2022 \[UW\]</u>\
System was unstable again\
New settings:\
![image-1b1677.png](2020-11-vecsel-2-heidi.attachments/image-1b1677.png)

------------------------------------------------------------------------

<u>01.02.2022 \[UW\]</u>\
System was stable until about 5:50 h this morning. Mode jumps began.\
Pump to 28.8 A and let it settle...\
![image-33a26a.png](2020-11-vecsel-2-heidi.attachments/image-33a26a.png)only 350 mW on dye table..., and still jumpy\
<u>01.02.2022 \[UW\]</u>\
Readjust BRF and ET and tune temperature settings.\
900mW out of LBO and 450 mW in VIS on dye laser table.\
![image-e755fb.png](2020-11-vecsel-2-heidi.attachments/image-e755fb.png)

------------------------------------------------------------------------

<u>16.11.2021 \[UW\]</u>\

- Closing cavity again without filters (pump at 29 A)\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>PD at setting 3<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-633219.png" alt="image-633219.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-3f88a3.png" alt="image-3f88a3.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-0abd95.png" alt="image-0abd95.png" /></td>
</tr>
<tr>
<td>Install BRF<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-b0c4c6.png" alt="image-b0c4c6.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-91451c.png" alt="image-91451c.png" /></td>
</tr>
<tr>
<td>PD at setting 2<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-1dd0ca.png" alt="image-1dd0ca.png" /></td>
<td></td>
</tr>
<tr>
<td>Install etalon<br />
tune brf and etalon to get about 12V on PD<br />
</td>
<td>about 2 W NIR before optical isolator<br />
</td>
<td></td>
</tr>
</tbody>
</table>

<u>15.11.2021 \[UW\]</u>\

- - Took out etalon and BRF\
  - Tweaked cavity mirror for lasing (at 33 A)\
  - moved pump spot on gain chip for max. NIR output power (using monitor PD)\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>New best spot!<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-c0c158.png" alt="image-c0c158.png" /></td>
</tr>
</tbody>
</table>

- - 15:00h Turned down pump to 20 A\
  - Tried to install BRF and etalon -- not successful.\
  - Cleaned etalon and BRF\
  - Decided to equip BRF with addon:\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>BRF clued to addon using<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-827405.png" alt="image-827405.png" /></td>
</tr>
<tr>
<td>Final<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-6b7e07.png" alt="image-6b7e07.png" /></td>
</tr>
</tbody>
</table>

<u>10.11.2021 \[UW\]</u>\

- - Significant power drop in the NIR output (onyl 1.2 W left)\
  - retuned optical elements\
  - system very unstable – what is wrong?\
  - Decided to put system out of order – Dye laser back to life.\

------------------------------------------------------------------------

05.10.2021 retuned optical elements for more stable (less mode jumps) and higher power.\
![Screen Shot 2021-10-05 at 11.02.48.png](2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-10-05%20at%2011.02.48.png)

------------------------------------------------------------------------

2021.09.14\
15:10h Water cooling of VECSEL#2 & \#3 now in series!\
![image-f19e80.png](2020-11-vecsel-2-heidi.attachments/image-f19e80.png)![image-4ba662.png](2020-11-vecsel-2-heidi.attachments/image-4ba662.png)2021.09.08+\
Check stability of pump diode current via OSTECH controller  reading\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Limited by  ADC?!<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-1de118.png" alt="image-1de118.png" /></td>
</tr>
<tr>
<td>Short term stability better than<br />
</td>
<td>2.9(1) x 10^(-4) A<br />
approx. 1.1 x 10^(-5)<br />
</td>
</tr>
<tr>
<td>for &lt; 1 s better than<br />
</td>
<td>approx. 2 mA <br />
approx. 7.7 x 10^(-5)<br />
</td>
</tr>
</tbody>
</table>

updated table:\

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="5"><strong><u>Stability limit estimates</u></strong><br />
</td>
<td>Comments<br />
</td>
</tr>
<tr>
<td>Element<br />
</td>
<td>Sensitivity<br />
</td>
<td>Noise amplitude est. (near 1.5 s)<br />
</td>
<td>Short term stability limits<br />
(near 1.5 s)<br />
</td>
<td>Est. of dominating noise bandwidth<br />
</td>
<td></td>
</tr>
<tr>
<td>Gain chip (via peltier) temperature<br />
</td>
<td>621(10) MHz/K<br />
</td>
<td>∆T_rms  = 3.2(3) mK<br />
</td>
<td>1.98(3) MHz<br />
</td>
<td>0-100 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Pump current (at 26 A)<br />
</td>
<td>44(2) MHz/A<br />
</td>
<td>∆A_rms =  0.29(1) mA<br />
</td>
<td>0.13(1) MHz<br />
</td>
<td>0 – 100 kHz<br />
</td>
<td>JD checks with Ostech for noise specs - 25.08.2021<br />
</td>
</tr>
<tr>
<td>Cold plate temperature<br />
</td>
<td>425(2) MHz/K<br />
</td>
<td>∆T_rms  = 0.42(3) mK (?)<br />
</td>
<td>0.18(2) MHz<br />
</td>
<td>0 – 0.5 Hz<br />
</td>
<td>Is the temperature that stable?<br />
</td>
</tr>
<tr>
<td>PZT voltage<br />
</td>
<td>71(1) MHz/V<br />
</td>
<td>∆V_rms &lt; 0.01 V<br />
</td>
<td>&lt; 0.71(1) MHz<br />
</td>
<td>0–10 kHz<br />
</td>
<td>Depends on electric filtering and driver specs<br />
</td>
</tr>
<tr>
<td>BRF temperature<br />
</td>
<td>&lt; 28(7) MHz/K<br />
</td>
<td>∆T_rms  = 4.0(4) mK<br />
</td>
<td>0.11(3) MHz<br />
</td>
<td>&lt; 1 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Etalon temperature<br />
</td>
<td>&lt; 29(14) MHz/K<br />
</td>
<td>∆T_rms  = 3.7(3) mK<br />
</td>
<td>0.11(6) MHz<br />
</td>
<td>&lt; 1 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Mechanical<br />
</td>
<td>?<br />
</td>
<td>?<br />
</td>
<td>?<br />
</td>
<td>0-10 kHz<br />
</td>
<td></td>
</tr>
<tr>
<td colspan="3"><strong>Sum of all effects:</strong><br />
</td>
<td><strong>&lt; 2.1(2) MHz</strong><br />
</td>
<td><strong>0-100 kHz</strong><br />
</td>
<td></td>
</tr>
<tr>
<td colspan="3"><em>Measured frequency stability:</em><br />
</td>
<td><em>2.5(1) MHz</em><br />
</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

2021-08-30ff\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>16:00h Recabling:<br />
VECSEL locked to LBO cavity to reduce short term noise (&lt;1 s)<br />
And locked to wave meter to stabilise on long terms (&gt; 1 s). Oscillations – PID parameters not optimal.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-7b7ec2.png" alt="image-7b7ec2.png" /></td>
</tr>
<tr>
<td>here without longterm stabilisation.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-33492c.png" alt="image-33492c.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-d7b318.png" alt="image-d7b318.png" /></td>
</tr>
<tr>
<td>20:00h: Back to previous cabling<br />
</td>
<td></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2021-08-26ff</u>\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>22:00 h<br />
GC 29.35<br />
BRF 36.5<br />
ET 45.8<br />
Sensitivity of NIR freq. to temp changes of GC, BRF, and Etalon<br />
&lt; 621(10) MHz/K<br />
&lt; 28(7) MHz/K<br />
&lt; 29(14) MHz/K<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-82ace8.png" alt="image-82ace8.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-3865cf.png" alt="image-3865cf.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-7c0a6d.png" alt="image-7c0a6d.png" /></td>
<td></td>
</tr>
<tr>
<td>Stability limits on short terms:<br />
<u>GC: 1.98(3) MHz</u><br />
BRF: 0.11(3) MHz<br />
ET: 0.11(6) MHz<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-c55fa3.png" alt="image-c55fa3.png" /></td>
<td></td>
</tr>
<tr>
<td>2021-08.27 7:00<br />
Pump laser ON - OFF - ON and monitor TEC voltages<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-b57363.png" alt="image-b57363.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-913a4f.png" alt="image-913a4f.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-293ad6.png" alt="image-293ad6.png" /></td>
</tr>
<tr>
<td>GC 29.35<br />
BRF 36.5<br />
ET 45.8<br />
Sensitivity of NIR freq. to PZT voltage and pump current<br />
71(1) MHz/V<br />
44(2) MHz/A<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-10706c.png" alt="image-10706c.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-2e6af2.png" alt="image-2e6af2.png" /></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="5"><strong><u>Stability limit estimates</u></strong><br />
</td>
<td>Comments<br />
</td>
</tr>
<tr>
<td>Element<br />
</td>
<td>Sensitivity<br />
</td>
<td>Noise amplitude est. (near 1.5 s)<br />
</td>
<td>Short term stability limits<br />
(near 1.5 s)<br />
</td>
<td>Est. of dominating noise bandwidth<br />
</td>
<td></td>
</tr>
<tr>
<td>Gain chip (via peltier) temperature<br />
</td>
<td>621(10) MHz/K<br />
</td>
<td>∆T_rms  = 3.2(3) mK<br />
</td>
<td>1.98(3) MHz<br />
</td>
<td>0-100 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Pump current (at 26 A)<br />
</td>
<td>44(2) MHz/A<br />
</td>
<td>∆A_rms = 0.1%<br />
</td>
<td>1.1(1) MHz<br />
</td>
<td>0 – 100 kHz<br />
</td>
<td>JD checks with Ostech for noise specs - 25.08.2021<br />
</td>
</tr>
<tr>
<td>Cold plate temperature<br />
</td>
<td>425(2) MHz/K<br />
</td>
<td>∆T_rms  = 0.42(3) mK (?)<br />
</td>
<td>0.18(2) MHz<br />
</td>
<td>0 – 0.5 Hz<br />
</td>
<td>Is the temperature that stable?<br />
</td>
</tr>
<tr>
<td>PZT voltage<br />
</td>
<td>71(1) MHz/V<br />
</td>
<td>∆V_rms &lt; 0.01 V<br />
</td>
<td>&lt; 0.71(1) MHz<br />
</td>
<td>Depends on electric filtering and driver specs<br />
</td>
<td></td>
</tr>
<tr>
<td>BRF temperature<br />
</td>
<td>&lt; 28(7) MHz/K<br />
</td>
<td>∆T_rms  = 4.0(4) mK<br />
</td>
<td>0.11(3) MHz<br />
</td>
<td>&lt; 1 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Etalon temperature<br />
</td>
<td>&lt; 29(14) MHz/K<br />
</td>
<td>∆T_rms  = 3.7(3) mK<br />
</td>
<td>0.11(6) MHz<br />
</td>
<td>&lt; 1 Hz<br />
</td>
<td></td>
</tr>
<tr>
<td>Mechanical<br />
</td>
<td>?<br />
</td>
<td>?<br />
</td>
<td>?<br />
</td>
<td>0-10 kHz<br />
</td>
<td></td>
</tr>
<tr>
<td colspan="3"><strong>Sum of all effects:</strong><br />
</td>
<td><strong>&lt; 2.4(2) MHz</strong><br />
</td>
<td><strong>0-100 kHz</strong><br />
</td>
<td></td>
</tr>
<tr>
<td colspan="3"><em>Measured frequency stability:</em><br />
</td>
<td><em>2.5(1) MHz</em><br />
</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

*<u>Noise of VECSELs are well described in literature, see e.g.</u>* \[<https://www.spiedigitallibrary.org/proceedings/Download?urlId=10.1117%2F12.1000329>\]*<u>:</u>*\
“The experimental work that we performed lead to the fact that VeCSELs are mainly concerned by various technical noise sources. First of all the pump noise : it is obvious that the pump noise acts like an intensity modulator for the laser (see eq. 2). The transfer function H(Ω) of the laser amplifies the pump noise and reports it on the emitted laser beam. At high pump rate, this gain asymptotically reaches the value of 1 over the flat-band of H(Ω). This pump noise can also be transferred to index fluctuations in the VeCSEL semiconductor chip through its thermal response. Indeed, instantaneous pump fluctuations produce temperature variations in the structure at low frequencies (lower than 100kHz). These temperature variations lead to index fluctuations in the structure, inducing cavity length fluctuations which are reported on the output beam as frequency fluctuations (thus noise). Moreover, the average temperature itself induces temperature fluctuations (the unavoidable ”thermal noise”), which contribute to the frequency noise too. Independently cavity length fluctuations may come from acoustic / mechanical vibrations.”\

------------------------------------------------------------------------

<u>2021-08-16ff</u>\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Mon<br />
</td>
<td>used for pi without new problems<br />
</td>
<td></td>
</tr>
<tr>
<td>Tue<br />
</td>
<td>JD installed a "new" chiller:<br />
<img src="2020-11-vecsel-2-heidi.attachments/image-c38662.png" alt="image-c38662.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-f60dc7.png" alt="image-f60dc7.png" /></td>
</tr>
<tr>
<td>another temp. sensor at base plate<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-822abf.png" alt="image-822abf.png" /></td>
<td></td>
</tr>
<tr>
<td></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-853ee5.png" alt="image-853ee5.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-80f41f.png" alt="image-80f41f.png" /></td>
<td></td>
</tr>
<tr>
<td></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-fbb376.png" alt="image-fbb376.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-225b58.png" alt="image-225b58.png" /></td>
<td></td>
</tr>
<tr>
<td></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-bda281.png" alt="image-bda281.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-a3a321.png" alt="image-a3a321.png" /></td>
<td></td>
</tr>
<tr>
<td>17:10 h<br />
Pump beam approx. 17.9 W<br />
Turn off the pump beam at  duration 10 s<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-833773.png" alt="image-833773.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-4e0c11.png" alt="image-4e0c11.png" /></td>
</tr>
<tr>
<td>Pump beam approx. 17.9 W<br />
Turn off the pump beam at  duration 8 s and back on at dur. 32 s<br />
<a href="2020-11-vecsel-2-heidi.attachments/VECSEL_2_2021_08_18_17_21_05.npy">VECSEL_2_2021_08_18_17_21_05.npy (application/octet-stream)</a></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-7b06e3.png" alt="image-7b06e3.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-f4b814.png" alt="image-f4b814.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-201529.png" alt="image-201529.png" />Peltier specs:<br />
<img src="2020-11-vecsel-2-heidi.attachments/image-2a1c10.png" alt="image-2a1c10.png" /></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2021-08-09ff</u>\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td colspan="3">Monday (09.08.2021)<br />
</td>
</tr>
<tr>
<td>21:30 h<br />
System is quite jumpy and needs hands on:<br />
Significant rotation of the BRF leads to significant more stable and tuneable system.<br />
</td>
<td>NEW parameter settings:<br />
Pump current: 25 A (Temp:25 °C)<br />
GC / BRF / ETALON:<br />
<img src="2020-11-vecsel-2-heidi.attachments/image-a2660d.png" alt="image-a2660d.png" />Pick up  PD: 8.5-8.8 V<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-86e854.png" alt="image-86e854.png" /></td>
</tr>
<tr>
<td colspan="3">Tuesday (10.08.2021)<br />
</td>
</tr>
<tr>
<td>11:00 h<br />
</td>
<td>Install thermistor on cold plate and monitor with Arroyo controller of VECSEL #3 ch2<br />
Steinhart-Hart-Coeff.:<br />
<img src="2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-08-10%20at%2015.40.12.png" alt="Screen Shot 2021-08-10 at 15.40.12.png" /></td>
<td>https://docs.rs-online.com/9fc4/0900766b8142cdf1.pdf<br />
</td>
</tr>
<tr>
<td>16:00 h<br />
cold plate temperature changes within 15 min<br />
from 15.8°C to 17.9°C<br />
</td>
<td>Est. drift approx. <strong><u>60 MHz/0.1°C</u></strong><br />
<strong><u>High rate of temperature change</u></strong><br />
<img src="2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-08-10%20at%2016.05.34.png" alt="Screen Shot 2021-08-10 at 16.05.34.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-c53ab5.png" alt="image-c53ab5.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-733aa3.png" alt="image-733aa3.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-72d0f4.png" alt="image-72d0f4.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-796061.png" alt="image-796061.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-47a507.png" alt="image-47a507.png" /></td>
</tr>
<tr>
<td colspan="3">Wednesday (11.08.2021)<br />
</td>
</tr>
<tr>
<td>11:55 h<br />
JD changed chiller temperature paras<br />
</td>
<td>Setpoint: 18C<br />
Lo: 17.5C<br />
Hi: 19C<br />
</td>
<td></td>
</tr>
<tr>
<td>16 h<br />
Take some data of the cold plate temperature and the VIS freq. (MHz)<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-2cac5f.png" alt="image-2cac5f.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-fe5b6a.png" alt="image-fe5b6a.png" /></td>
</tr>
<tr>
<td>Short term (2 Min):<br />
Chiller temperature set point: <strong><u>18.0 °C</u></strong><br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-bf922d.png" alt="image-bf922d.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-60a975.png" alt="image-60a975.png" /></td>
</tr>
<tr>
<td></td>
<td colspan="2"><img src="2020-11-vecsel-2-heidi.attachments/image-b4164b.png" alt="image-b4164b.png" /></td>
</tr>
<tr>
<td>Mid term (60 Min):<br />
Chiller temperature set point: <strong><u>18.0 °C</u></strong><br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-15afbf.png" alt="image-15afbf.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-8a922a.png" alt="image-8a922a.png" /></td>
</tr>
<tr>
<td></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-a16c16.png" alt="image-a16c16.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-348930.png" alt="image-348930.png" /></td>
</tr>
<tr>
<td></td>
<td colspan="2"><img src="2020-11-vecsel-2-heidi.attachments/image-ce8755.png" alt="image-ce8755.png" /></td>
</tr>
<tr>
<td>20:58 h<br />
We now track also the temperatures of the gain chip, BRF, and Etalon<br />
short term test – 2 min<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-d78c35.png" alt="image-d78c35.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-db058e.png" alt="image-db058e.png" /></td>
</tr>
<tr>
<td>90 Min:<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-eb2b9a.png" alt="image-eb2b9a.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-f07fbe.png" alt="image-f07fbe.png" /></td>
</tr>
</tbody>
</table>

<u>2021-07-05ff</u>\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Mon<br />
</td>
<td><ul>
<li>Turn on system (warm up of 1 hour) by DP<br />
</li>
<li>Output powers (10:45h): NIR after fibre 1.25 W; 500 mW VIS; 260 mW on Dye table<br />
</li>
<li>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP. <br />
</li>
</ul></td>
<td>VECSEL-PIEZO specs [https://www.physikinstrumente.store/eu/p-080.311/]:<br />
<img src="2020-11-vecsel-2-heidi.attachments/image-7fd695.png" alt="image-7fd695.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-dabf4a.png" alt="image-dabf4a.png" /></td>
</tr>
<tr>
<td>Tue.. Wed<br />
</td>
<td>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP. <br />
</td>
<td></td>
</tr>
<tr>
<td>Thu<br />
</td>
<td>Power outage over night. Temp. control and pump was shut off. JD rebooted things. DP used it as Photo.<br />
</td>
<td></td>
</tr>
<tr>
<td>Fri<br />
</td>
<td>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP. <br />
</td>
<td></td>
</tr>
</tbody>
</table>

<u>2021-06-28ff</u>\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Mon<br />
</td>
<td><ul>
<li>Turn on system (warm up of 1 hour)<br />
</li>
<li>Fine tune etalon temp to 46.17 °C &amp; Adjust VECSEL head piezo to get to 262.70290 THz<br />
</li>
<li>LBO now locked via Brückner box – problems with RedPitaya power supply<br />
</li>
<li>Output power (500 mW in VIS) and freq. (near 525.40580 THz) stable over more than 2 hours<br />
</li>
</ul></td>
</tr>
<tr>
<td>Tue<br />
</td>
<td>8:30<br />
&#10;<ul>
<li>System jumpy, adjust piezo to get back to near 525.40580 THz<br />
</li>
</ul>
8:45<br />
&#10;<ul>
<li>2.7 W /  2.15 W /  2.0 W / 1.2 W / .47 W (VIS); system very jumpy, tune ET back to 46.15 °C<br />
</li>
</ul>
Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP. <br />
</td>
</tr>
<tr>
<td>Wed<br />
</td>
<td>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP.<br />
</td>
</tr>
<tr>
<td>Thu<br />
</td>
<td>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by FH and DP.<br />
</td>
</tr>
<tr>
<td>Fri<br />
</td>
<td>Overall a few jumpy moments (fixed by piezo tuning), but it was used throughout the day for loading by DP. DP turned off system<br />
</td>
</tr>
</tbody>
</table>

<u>2021-06-23</u>\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>New parameter settings and first day of duty for BERMUDA &amp; PAULA<br />
<strong><u>Pump @ 25 A</u></strong><br />
<strong><u>GC 30.0 °C</u></strong><br />
<strong><u>BRF 41.7 °C</u></strong><br />
<strong><u>Etalon 46.15 °C</u></strong><br />
</td>
<td>Paula loaded at 10:30 h<br />
Bermuda loaded several times before lunch.<br />
</td>
</tr>
<tr>
<td>11:50<br />
</td>
<td>Diff. PD of LBO died?!<br />
Try to find replacement... Broken SMA cable fixed.<br />
working again<br />
</td>
</tr>
<tr>
<td>16:30<br />
</td>
<td>Turned off the system and switched back to dye laser until next week.<br />
</td>
</tr>
</tbody>
</table>

<u>2021-06-21+22</u>\

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>10:30 h – Status<br />
</td>
<td>NIR 2.85 W<br />
NIR into fibre 2.2 W<br />
NIR out of fibre 1.1 W<br />
VIS 350 mW<br />
</td>
<td></td>
<td></td>
</tr>
<tr>
<td>11:00 Installed wave plates before fibre.<br />
</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>13:35 Checked main fibre coupler to LBO (<u>60FC-F-4-A4-M5-33 – about 50 % coupling eff.</u>) and exchange with wave meter port (<u>60FC-F-4-A4.5S-03 – about 65 % coupling eff</u>)<br />
BUT: Get a new fibre coupler. Maybe:  <u>60FC-F-4-A5S-03?!</u><br />
</td>
<td>NIR out of fibre 1.4 W<br />
<strong><u>VIS 590 mW</u></strong><br />
</td>
<td></td>
<td></td>
</tr>
<tr>
<td>15:15h VIS fibre coupling (60FC-SF-) about <strong><u>60 %</u></strong> good enough for now;<br />
</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>16:25 First ion loading in EUROTRAP with new light!</strong><br />
(with a hacky fibre coupling &amp; VECSEL freq. free running)<br />
NEXT: Overlap VECSEL light with dye laser to get it into  fibre couplin area for PUALA, BERMUDA, and wave meter , and I2 spec.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-06-21%20at%2016.30.13.png" alt="Screen Shot 2021-06-21 at 16.30.13.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong><u>17:45</u></strong>  Sneak in of the VECSEL#1 photo: Light is  send into the dye laser beam path for light distribution via a removable mirror:<br />
&#10;<ol>
<li>Wavemeter / I2 spectroscopy (<u>~10 mW</u>)<br />
</li>
<li>PAULA (<u>~130 mW</u>)<br />
</li>
<li>BERMUDA (<u>~130 mW</u>)<br />
</li>
</ol></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-06-22%20at%2008.24.12.png" alt="Screen Shot 2021-06-22 at 08.24.12.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td>PAULA and BERMUDA should be able to load without power redistributions.<br />
</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong><u>2021-06-22 8:00</u></strong><br />
NOTE: Freq. drift problem of VECSEL head requires improvement, cp. (wave meter log: 22.06.2021, 08.15,  525,4059122 THz)<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-1bf60e.png" alt="image-1bf60e.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-175805.png" alt="image-175805.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong><u>9:30</u></strong> Change chiller set temp to <strong><u>18.0 °C</u></strong> after discussion with L.G.<br />
</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong><u>9:50</u></strong> Check freq drifts in <u>NIR</u> with wave meter<br />
Stab. on 1 sec: <strong><u>2.2(1) MHz</u></strong> Hmm, not great! Why?<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-ef5c76.png" alt="image-ef5c76.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-9dd40b.png" alt="image-9dd40b.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong><u>10:00</u></strong> Check freq drifts in <u>VIS</u> with wave meter (22.06.2021, 10.11,  525,4057168 THz_m.lta)<br />
Stab. on 1 sec: <strong><u>4.2(1) MHz</u></strong> Hmm, not great! Why?<br />
Change in chiller set temp improved drift by about <strong><u>10x</u></strong><br />
<strong><u>NOTE:</u></strong> Over the course of tens of minutes still jumpy. Check temperature stability of different elements.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-d15ec9.png" alt="image-d15ec9.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-06bbff.png" alt="image-06bbff.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chiller details:<br />
Set temp: <strong><u>18.0 °C.</u></strong><br />
Reading varies by more than <strong><u>~2 °C</u></strong><br />
Spec sheet: <a href="https://www.lauda.de/pimimport/assets/context/pdmarticle/85/8575/8575/attachments/Export.8575.2018-10-11-16-44-56.70df7639.pdf">https://www.lauda.de/pimimport/assets/context/pdmarticle/85/8575/8575/attachments/Export.8575.2018-10-11-16-44-56.70df7639.pdf</a><br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-196c4b.png" alt="image-196c4b.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-09a16b.png" alt="image-09a16b.png" /><em>Assembly detail of water-cooled block. Isolation from base plate may need to be improved!?</em><br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-62fb40.png" alt="image-62fb40.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-32a086.png" alt="image-32a086.png" /></td>
<td><a href="2020-11-vecsel-2-heidi.attachments/Q4DT-E_13-001%20Microcool_V6REV17_EN_translation.pdf">Q4DT-E_13-001 Microcool_V6REV17_EN_translation.pdf (application/pdf)</a></td>
</tr>
<tr>
<td>11:45 Free running long term 30+ min<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-6e50e0.png" alt="image-6e50e0.png" /></td>
<td></td>
<td></td>
</tr>
<tr>
<td>12:25 Test of wavemeter lock (LG settings of VECSEL #1)<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-d17ab8.png" alt="image-d17ab8.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-5a50f5.png" alt="image-5a50f5.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-caf0cc.png" alt="image-caf0cc.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-390c6b.png" alt="image-390c6b.png" /></td>
<td></td>
</tr>
<tr>
<td>12:45 Auto find of PID parameters for Etalon temp.<br />
</td>
<td>not successful<br />
</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2021-06-17 \[UW\]</u>\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><strong><u>00:30</u></strong><br />
First yellow at LBO temp approx <strong><u>75 °C</u></strong><br />
LBO cavity is locking and delivering about <strong><u>5 mW (VIS)</u></strong> for <strong><u>approx. 100 mW (NIR)</u></strong> in.<br />
NEXT:<br />
&#10;<ul>
<li>Install build up PD.<br />
</li>
<li>Tweak up of fibre coupling, mode matching, and LBO temp.<br />
</li>
</ul></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-eb7424.png" alt="image-eb7424.png" /></td>
</tr>
<tr>
<td>L.G. estimated the req. Temp. of the LBO [<span>Temperature-Tuned 90° PhaseMatching Properties of LiB305 von K.Kato. </span><a href="https://ieeexplore.ieee.org/document/362711">https://ieeexplore.ieee.org/document/362711</a><span> </span>]<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/PastedGraphic-2.png" alt="PastedGraphic-2.png" /></td>
</tr>
<tr>
<td>15:30 Status:<br />
New Vecsel head parameter:<br />
(see Labbook, update next week)<br />
Fibres:<br />
NIR: to Wave meter and LBO<br />
VIS: one fibre coupler installed needs  tweak<br />
For about <strong><u>900 mW</u></strong> NIR in front of LBO, we get <strong><u>340 mW</u></strong> of VIS at <strong><u>525.40580 THz.</u></strong><br />
Efficiency about <strong><u>42 %/W.</u></strong><br />
NEXT WEEK: See keywords on image.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/Screen%20Shot%202021-06-18%20at%2015.32.01.png" alt="Screen Shot 2021-06-18 at 15.32.01.png" /></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2021-06-17 \[UW\]</u>\

- Glueing 250 mm lens for beam collimation after head.\
- get light into wavemeter\

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>11:35<br />
quick setup for fibre coupling to wave meter<br />
BRF &amp; Etalon tuning does not get us closer to  the req. 262.70 THz<br />
NEXT: change gain chip temp.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-dd9e46.png" alt="image-dd9e46.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-7c05d2.png" alt="image-7c05d2.png" /></td>
</tr>
<tr>
<td>11:40 adjust temp:<br />
GChip <u>30.0°C</u><br />
BRF <u>35.5 °C</u><br />
ETALON <u>not working?! loose connection in VECSEL head (see pic)</u><br />
getting closer...<br />
pump @ <u>23 A</u><br />
NIR after head: <u>2.2 W</u><br />
Still quite jumpy btw <u>262.52 THz– 262.86 THz</u><br />
NEXT: connect cavity piezo<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-db1057.png" alt="image-db1057.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-5b27b7.png" alt="image-5b27b7.png" /></td>
</tr>
<tr>
<td>15.55 further tweak now with etalon temp control.<br />
CHECK – let see for how long we can stick around here.<br />
output: <strong><span><u>2.8 W</u></span></strong><br />
NEXT: install optical isolator.<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-510d03.png" alt="image-510d03.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-fcddbe.png" alt="image-fcddbe.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-0efdf6.png" alt="image-0efdf6.png" /></td>
</tr>
<tr>
<td>16:45<br />
Optical isolator installed and optimised, but <strong><u>ONLY</u></strong> in forward direction!<br />
<strong><u>OUT 2.35 W vs IN 2.85 W</u></strong><br />
approx. <strong><u>82.5 %</u></strong><br />
NEXT: Move AGILE LBO into place and get some yellow<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-5a9616.png" alt="image-5a9616.png" /></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2021-06-16 \[UW\]</u>\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Labbook<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image.png" alt="image.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-cf3f88.png" alt="image-cf3f88.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/Untitled.svg" alt="Untitled.svg" /><img src="2020-11-vecsel-2-heidi.attachments/Untitled-47361f.svg" alt="Untitled-47361f.svg" /><em><u>PD cal:</u></em><br />
<span>PWR/U_PD =  <u>3.1(2) W/V</u></span><br />
</td>
</tr>
<tr>
<td>Photos<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-e006c5.png" alt="image-e006c5.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-f623ce.png" alt="image-f623ce.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/image-7b79b0.png" alt="image-7b79b0.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-9b0478.png" alt="image-9b0478.png" /><img src="2020-11-vecsel-2-heidi.attachments/image-47f7c8.png" alt="image-47f7c8.png" /></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<u>2021-03-11:</u>\

- Adjusted cavity without frequency filters:\
- For details see lab book\

![Bildschirmfoto 2021-03-11 um 16.46.01.png](2020-11-vecsel-2-heidi.attachments/Bildschirmfoto%202021-03-11%20um%2016.46.01.png)\[UW\]: Nice!\
<u>2020-12-02:</u>\
<u>Adjustment of pump beam:</u>\

- use RND endoscope camera to monitor pump beam on gainchip (with 3A pump current you get a nice signal)\
- translate focuser such that the pump spots diameter is minimal\
- fix the focuser inside the mirror mount with the 2 screws (grub screws with nylon tip)\
- shake fiber a bit and check whether spot is not moving\
- use mirror mount to adjust pump spot at the center of the gainchip\

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><img src="2020-11-vecsel-2-heidi.attachments/3AD34371-CD8D-4146-B48F-C20D733CB303_1_105_c.jpeg" alt="3AD34371-CD8D-4146-B48F-C20D733CB303_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/20170307105333.jpg" alt="20170307105333.jpg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/Bildschirmfoto%202020-12-02%20um%2015.34.11.png" alt="Bildschirmfoto 2020-12-02 um 15.34.11.png" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/20170307105521.jpg" alt="20170307105521.jpg" /></td>
</tr>
<tr>
<td>position of pump focuser<br />
</td>
<td>pump spot with a pump current of 3A<br />
</td>
<td>zoom<br />
</td>
<td>pump current 9A<br />
</td>
</tr>
</tbody>
</table>

<u>Adjustment of cavity</u>\

- shoot an collimated red laser beam through the out coupler mirror onto the gain chip\
- make sure that you hit the gain chip as well as the output coupler at the center\
- adjust the OC mirror such that the the beam is reflected into itsself\
- check at different positions and iterate as long as necessary\
- i had to loose the screws between cooling block and Invar baseplate\
- an aperture might help you\
- beam heigth outside case is nominally 83.1mm\

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td><img src="2020-11-vecsel-2-heidi.attachments/B9117B85-7B9F-4F83-B1B7-0CE9228ED1DF_1_105_c.jpeg" alt="B9117B85-7B9F-4F83-B1B7-0CE9228ED1DF_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/D52EEE4F-4A12-4E56-8623-CB0AF6886259_1_105_c.jpeg" alt="D52EEE4F-4A12-4E56-8623-CB0AF6886259_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/08D1FA00-21E3-498C-8954-8CD52BE7F5FC_1_105_c.jpeg" alt="08D1FA00-21E3-498C-8954-8CD52BE7F5FC_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/94AC1E31-6DBB-481D-824E-87E5515AE2B4_1_105_c.jpeg" alt="94AC1E31-6DBB-481D-824E-87E5515AE2B4_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/CE77C226-621F-4F9D-85AD-AAED370F970C_1_105_c.jpeg" alt="CE77C226-621F-4F9D-85AD-AAED370F970C_1_105_c.jpeg" /></td>
</tr>
<tr>
<td>hit gainchip at center<br />
</td>
<td>it OC mirror at center<br />
</td>
<td>hit hole inside case at center<br />
</td>
<td>make sure that beam is reflected into itself at different points, e.g. at this mirror... <br />
</td>
<td>...and at an additional aperture<br />
</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<u>2020-12-01:</u>\
<u>Assembly of gainchip (# XXXXXXX):</u>\

- pump light focuser was not removed, pay attention not to touch it\
- standard mounting procedure with feed throughs at bottom\
- a bit tricky because screws for gainchip require access through feed throughs\
- put silicon free thermal compound on both sides of Peltier\
- remove label and remaining glue on gainchip with a acetone tissue before\
- put gainchip on top of peltier\
- fix it with 4 screws\
- wrap some indium around temperature sensor\
- put it into slit in clamp\
- mount clamp, pay attention for gain chip\
- fix it with 4 screws, make sure not to damage the temperature sensor\
- close feedthroughs\
- put lid on case\
- done\

<u>Final result:</u>\
![18D656C6-A54F-4042-8A9E-AE54F2A97CB7_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/18D656C6-A54F-4042-8A9E-AE54F2A97CB7_1_105_c.jpeg)

------------------------------------------------------------------------

<u>2020-11-30:</u>\
<u>Analyzing Temperatures inside VECSEL 2.0</u>\

- measurment similar to 2020-11-27\
- but now maximal pump power of approx 40W\
- Labbook:\

|  |  |
|----|----|
|  | [doc04621020201201085618.pdf (application/pdf)](2020-11-vecsel-2-heidi.attachments/doc04621020201201085618.pdf) |
|  |  |

Some images:\

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td>Chosen pump laser parameters<br />
</td>
<td>Arrangement of pump laser<br />
</td>
<td>Hottest guy at lab<br />
</td>
<td>Temperatures inside VECSEL after 1h operation at 40W<br />
</td>
<td>Visible image after Test<br />
</td>
<td></td>
</tr>
<tr>
<td><img src="2020-11-vecsel-2-heidi.attachments/5492C871-81A4-4FA5-9AE8-2697BDA5550A_1_105_c.jpeg" alt="5492C871-81A4-4FA5-9AE8-2697BDA5550A_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/7B65BD20-16FC-46A5-8DDB-E680F9594A64_1_105_c.jpeg" alt="7B65BD20-16FC-46A5-8DDB-E680F9594A64_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/160E40B4-0300-4588-9A4C-D2400F1859C9_1_105_c.jpeg" alt="160E40B4-0300-4588-9A4C-D2400F1859C9_1_105_c.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/3BB49B63-E4DA-4FF2-B6C1-6BFF03B42871_1_201_a.jpeg" alt="3BB49B63-E4DA-4FF2-B6C1-6BFF03B42871_1_201_a.jpeg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/EA65711C-CDBE-4D8D-B73C-4221E4288564_1_105_c.jpeg" alt="EA65711C-CDBE-4D8D-B73C-4221E4288564_1_105_c.jpeg" /><img src="2020-11-vecsel-2-heidi.attachments/Bildschirmfoto%202020-12-01%20um%2009.07.19.png" alt="Bildschirmfoto 2020-12-01 um 09.07.19.png" /></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Note: during first run (transparent curtain closed) laser shut off after approx 15min with error 11- crystal temperatures exceeds upper limit.<br />
With setup shown above laser was running for approx 1h at 27 W and 1h at 40W without error.<br />
</td>
<td></td>
<td></td>
<td>Bottom: Laser engraving works<br />
</td>
<td></td>
</tr>
</tbody>
</table>

<u>Conclusions:</u>\

- measured temeperature deviations from gainchip set point below 3mK\
- New design of pump dump is not measurable (by hand) warmer than ambient temperature\
- Chiller temperature remains not in the specified (+-0.5K), maybe thermal load is too small?\
- Peltier power seems to be correlated to water temperature. Power changes less than 10%\
- Maybe add some load to cooling circuit to keep the temperature more constant?\
- Keep an eye on pump laser temperature, so far error occurred only once\

------------------------------------------------------------------------

<u>2020-11-27:</u>\
<u>Analyzing Temperatures inside VECSEL</u>\

- using dummy gainchip\
- focusing on center (3A pump current)\
- ![20170302091154.jpg](2020-11-vecsel-2-heidi.attachments/20170302091154.jpg)

<u>Checking pump reflections on beam dump:</u>\

- beam dump V1 is glued to cooling plate\
- new beam dump is screwed to clamp of gainchip, checking whether this could be disadvantageous below\

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Pump power<br />
</td>
<td>8A = 0.7 W<br />
</td>
<td>15A = 7.6W<br />
</td>
</tr>
<tr>
<td>Image with RND cam<br />
</td>
<td><img src="2020-11-vecsel-2-heidi.attachments/20170302091511.jpg" alt="20170302091511.jpg" /></td>
<td><img src="2020-11-vecsel-2-heidi.attachments/20170302091337.jpg" alt="20170302091337.jpg" /><img src="2020-11-vecsel-2-heidi.attachments/20170302091650.jpg" alt="20170302091650.jpg" /></td>
</tr>
</tbody>
</table>

-\> geometrical design of new pump dump looks good\
<u>Checking Temperature control circuit</u>\
Pump power: 20W (27A) \
T_gainchip set to 18°\
T_chiller set to 17°\
T_chiller was around 15.5° at t=0. Some thermalization would have been beneficial\

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>t<br />
</td>
<td>Peltier current (A)<br />
</td>
<td>Peltier voltage (V)<br />
</td>
<td>Chiller temp<br />
</td>
</tr>
<tr>
<td>0min<br />
</td>
<td>0.67<br />
</td>
<td>2.15<br />
</td>
<td>15.5<br />
</td>
</tr>
<tr>
<td>12 min <br />
</td>
<td>0.71<br />
</td>
<td>2.28<br />
</td>
<td></td>
</tr>
<tr>
<td>14 min<br />
</td>
<td>0.74<br />
</td>
<td>2.40<br />
</td>
<td></td>
</tr>
<tr>
<td>16 min<br />
</td>
<td>0.78<br />
</td>
<td>2.57<br />
</td>
<td></td>
</tr>
<tr>
<td>18 min<br />
</td>
<td>0.81<br />
</td>
<td>2.66<br />
</td>
<td>17.5<br />
</td>
</tr>
<tr>
<td>21 min<br />
</td>
<td>0.81<br />
</td>
<td>2.65<br />
</td>
<td>17.5<br />
</td>
</tr>
<tr>
<td>22 min<br />
</td>
<td>0.80<br />
</td>
<td>2.61<br />
</td>
<td>17.4<br />
</td>
</tr>
</tbody>
</table>

-\> changes in Peltier power consumptions most likely related to water temperature variations\
-\> set  and actual temperature (20°C) of gain chip was constant all the time\
<u>Some thermal images directly after turning off the laser (was running for 22min at 20W):</u>\
Comments:\

- images can be miss-interpreted e.g. due to reflections of the users body, especially at the polished Invar parts\
- therefore also don’t trust the absolute temperatures...\
- checking pump dump temperature by hand: feels like room temperature\
- checking pump light focuser by hand: temperature is increased but still touchable for minutes without burning your fingers\

|  |  |  |
|----|----|----|
| ![Bildschirmfoto 2020-11-27 um 14.44.19.png](2020-11-vecsel-2-heidi.attachments/Bildschirmfoto%202020-11-27%20um%2014.44.19.png) | ![20201127T140730.jpg](2020-11-vecsel-2-heidi.attachments/20201127T140730.jpg) | ![80D0A5AD-DC8C-4F91-BC6D-41657857874B_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/80D0A5AD-DC8C-4F91-BC6D-41657857874B_1_105_c.jpeg) |

-\> no inhomogenous heating of gainchip observable\
-\> check also at maximum power, but design of new pump dump looks promising.\

------------------------------------------------------------------------

<u>2020-11-26:</u>\

|  |  |  |  |  |
|----|----|----|----|----|
| ![7C60892A-5147-48C8-BD94-EEAA72A73D26_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/7C60892A-5147-48C8-BD94-EEAA72A73D26_1_105_c.jpeg) | ![D3D7F2F1-B340-4B58-A419-54FF6A187ECE_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/D3D7F2F1-B340-4B58-A419-54FF6A187ECE_1_105_c.jpeg) | ![C26BF26A-DC96-4F96-BA13-61AF0EFD72D0_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/C26BF26A-DC96-4F96-BA13-61AF0EFD72D0_1_105_c.jpeg) | ![17AF5794-DCC5-4574-BF81-7EFB3350B422_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/17AF5794-DCC5-4574-BF81-7EFB3350B422_1_105_c.jpeg) | ![2A45D7C8-9E34-482E-9473-8BD54FD06C52_1_105_c.jpeg](2020-11-vecsel-2-heidi.attachments/2A45D7C8-9E34-482E-9473-8BD54FD06C52_1_105_c.jpeg) |

Temperaturcontroller:\
IP: [internal IP redacted]\
Adresse: 00:80:A3:E2:6A:AF\
Bezeichnung: Temperaturcontroller Arroyo\
Vorschlag Hostname: [internal hostname redacted]\

- fiber focuser in mount, focus and position not adjusted\

------------------------------------------------------------------------

<u>2020-11-25:</u>\

- Aluminium Gainchip Dummy assembled in setup\
- Temperature control of Gainchipdummy inclusive water cooling tested\
