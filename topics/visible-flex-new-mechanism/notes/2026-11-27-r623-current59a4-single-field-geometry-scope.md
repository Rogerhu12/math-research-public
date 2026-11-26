# 当前59a4的一次实际材料场：新完整参考与全C0/C1/R623曲率

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

本文件是新声明的公开 Actions 计算范围与纸面接口说明，尚无本scope科学结果。
它接[normal298的实际59a4/f60终态](2026-11-27-r582-physical-pending298-original-terminal.md)，
并消费R623已证的有限vertical primitive，而不是重试旧a237的mesh标签。

## 1. 唯一当前输入与没有保存的边界

原run45901312947/job140187488430的完整FINAL479059 B，SHA
`8b6f57b0a4d0f212fe378c10ec563e350efa7ca2b0e7d958912715e25ce42e15`。
实际97q为`59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45`，
`p=.181`。真实材料为f60；完整finite资格16149×3072，eta3.838285782595128e-5、
physical/working violation0。原required16167尚未被该保留q完整核定，不能改写资格。

新input只引用已发布normal311 request（source181de62c735dfa087cd62e842c191c7d226f4e0a）的完整必要FINAL，核其字节/hash/唯一原来源，
不再存一份479k重复终态。q64:80与末位q96才定义当前mean；q80:96为额外tail列。
当前mean与旧a237已改变，旧mean圆rho/D及所有旧场delta/alpha均不使用。

必要material recipe仍是原4609B paid seed，使用原rtol2e-11、atol2e-13、
max_step.15、initial_epsilon.001和完整正图；原Frozen radius商不因选择新comparison
mean而变化。旧0d的真实全部endpoint/ODE分段dense状态从未保存；不能声称从小recipe
自动按字节恢复它。R623先前133.48344923899998秒的mesh mismatch费用保留。

## 2. 先认证当前mean的完整圆参考

使用真正当前q的8+8个mean控制及h=q96，圆core半径仍为.38。原R611 v2对象
只供应共享解析H的向外舍入积分；不消费旧圆曲率或旧叶结果。H仍是完整无限振荡积分，
没有把浮点seed的数值零suffix赋给mean。

新紧段从C=.036到向外覆盖的
$s_*=L-\ell(2/25)$，全部接口/样条节点在初始分割中，逐闭cell验证
$a\ge r_c=.22$、$z_s>0$、$a_s^2+z_s^2>0$和有效有限子午曲率盒。
目标$1/.06072$仅驱动细化；若超过目标，则只在$\kappa_{\rm lo}>0$
时允许$\kappa_{\rm hi}\le1.002\kappa_{\rm lo}$作为另一紧度条件。
到实际深度/细化容量后可以保留仍有效的较宽上界，不能裁掉上界；若正半径/单调高度/
正速度尚未证成，则cell unresolved，整体不完成。容量只停止细化，不截掉未访问区域。

全尾调用R608的既有解析定理，先对实际q64:80逐个准确核$|q_i|<3/5$：

1. 背景和紧支撑控制在尾区已准确到位，原样条/包络全尾显式界继续适用；
   改变常数h不影响任何尾导数。
2. 整个开尾$a\ge r_c$、$z_s>0$，$a_s\to-1$、$z_s\to0$，
   所有径向mean校正及$H$的相应jets在L全平。
3. R608全尾子午曲率上界小于$1/.06072$，尾半径不超过.237；完整平帽
   仍是半径.22的整个Cartesian圆盘，不用正宽annulus冒充圆盘。
4. 核心圆柱和常值collar的子午曲率为0、半径.38、z为原材料坐标；平坦
   过渡给C²拼接。下半体为原正交镜面，所有上半结论因此完整覆盖下半。

只有这些全域条件及紧段全覆盖都成立，才令
$$
 \bar\kappa=\max\{\bar\kappa_{\rm compact},1/.06072\},\qquad
 \rho=\min\{.06072,1/\bar\kappa\}
$$
并用向外舍入取得下界。这里不是仅从1/curvature推reach：已同时支付R599的
完整单值单调高度图、最低半径$a\ge r_c\ge\rho$、端法向极限、C²帽接点、
上下完整侧体和完整圆盘；R599给全法弦不等式与全闭曲面reach。其条件对更小rho
保持，不能把降低rho当作完成.03D门。

完整参考直径按$D_0\le2\sqrt{a_{\max}^2+h^2}$向外包住，a_max取紧段上界、
core .38和全尾.237的最大值；z单调使全体|z|≤h。新rho/D从本scope真正全覆盖取得。

## 3. 一次实际材料构造与必要物理资格

参考通过后只调用一次原ReconstructedField。记录真正actual mesh SHA，保存原
实际source、recipe、ODE/height/RHS和材料查询成本。构造失败也保留已存在对象的
counters与已花elapsed。

若actual SHA恰为原f60，则相同q、相同源定义/endpoint场的16149观察可以直接复用，
明确不是16167。若SHA不同，直接声明新的有限C²材料场，而非修改旧标签；同一个
Python对象同时供应全部fine与后续区间接口，绝不再造一个近似场来做资格。

异场时fine保留原全部16167坐标、311coarse/midpoints、该实际新field必要活跃
endpoint及midpoints的精确并集，角3072。每128径向点调用原hard.complete_scan，
同原FineObserver取所有八个物理组的最小裕量、mean-E/det/高度/面积下界、球/条带
和metric最大值，使用原mean_E_floor.25、det_floor.1、geometry_margin.001、
feasibility_tolerance1e-8及原box容差。无需把整网field数组长期堆在内存，标量
聚合和门与原程序相同，没有少算点或改变接受标准。

新的fine只给它真正处理的field与grid发资格，若失败仍保留失败的全观察且不伪称
当前新field通过物理门。若clock中断，输出已完成块、下一未处理索引、完整请求网格
身份和partial maxima，不能给局部报告贴全域标签。没有optimizer、AD/Jac或旧方向/
七点/多seed诊断。必要新物理资格与连续证书分别如实汇报。

## 4. 同一次cell数据得到新的全C0/C1/K

所有新的delta/alpha/K都在本scope取得；不借旧0d或旧a237的global cap。
每个cell只读一次完整径向coefficients和同当前mean的六jets；R623已证helper
同时给出完整u/v、四个真实v模式2/4/6/8的准确primitive界与非线性归一余项。
实际竖直切向仍是$v/\sqrt{1+v^2}$，绝不换为线性v。

设$P_h,P_v$是同cell的完整水平/竖直零均值primitive范数界，当前半径a，
直接相关差jets为da,dz。由
$\Delta\Phi=da\,e_r+dz\,e_z+a\,\mathcal P\Delta T$，得到
$$
 \|\Delta\Phi\|\le\sqrt{da^2+dz^2}
   +|a|\sqrt{P_h^2+P_v^2}.
$$
此式在源码全用区间算术。C1直接使用R623原函数已计算的未继承cap的local-alpha，
其中两个正交参考正交基方向使用Frobenius上界，因此包住operator norm。
K使用同cell R623法向分块界；其$\alpha<1$条件必须实际成立，失败只能细化或
unresolved。完整协变二阶差仍由h11,h12,h22的Frobenius范数报告，不用它驱动细化。

mean模块使用同q reference_q，直接差保留相关性；材料seed的design.reference_alpha
仍是原冻结半径，不能因为换圆参考就偷换seed。

## 5. 没有漏掉core/collar、接口、尾和帽

原p=.181、q=.18、offset=.2的完整角core界可从原已付FIELD5672B复用，因为所有
新的angular/mean校正都在[0,C]准确为零，tail gates也未开启。新field仍先通过
同一次[0,C]调用检查其**所有原Hermite core cells**真为A=.5、C=0和零一二jets；
不是仅凭p相同推断任意endpoint数据。该段的新C0/C1仍本次支付；其真实曲率可取
原完整core的1/rho_core（与同cell有效K界取小），中央柱按同材料z外推。

其余[C,L]保留全部实际Hermite cell和所有named interface，C交点按完整C²jets
拼接；literal .82与L−.08的两个不同binary64位置都保留。只在接口已经证明是
**原同一材料的准确零suffix**时合并剩余零多项式区间；解析mean尾仍不截断。
端点、相邻闭cell及完整Cartesian帽覆盖无缝；下半用原正交反射。

C0目标.0025、C1目标.03、K目标18都仅是细化目标。深度/细化容量达到后仍可汇总
有效的较宽上界；非有限、负界或未定义box永不接受。未闭队列和当前unresolved
cell连同已付partial maxima输出，未全覆盖便不给global bounds或reach结论。

## 6. 新完整近远法弦结论与费用

只在新reference和新全域norm/K都完成时用R604：$\nu=\alpha$、
$\lambda=1+\alpha$，K取本次完整R623上界。先用原短近程证书；只有短证书未建立，
或被far项限制且未过.03时，才消费R622较长近程。若短程已受1/K限制，.9/K不可能
改善，跳过；不拼接不同证书的阈值和near项，也不比较/沿用其他q或材料的旧证书。

新科学上限1800秒、预留30秒。一次必要height prefix共享于新圆和非圆mean；
一次必要field重建共享所有工作。原f1/a237几何、R623失败、全部optimizer历史及
更早未知成本继续保留，新的所有积分、ODE、区间、fine与未闭工作如实计入本scope。
不保存可重算的62878端点或leaf数据表，只输出必要小收据和真正未完任务状态。

本地只做纸面推导、源代码、AST、JSON和hash；没有导入或执行科学函数。

## 7. 执行绑定

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `topics/visible-flex-new-mechanism/scripts/r623_current59a4_single_field_geometry_20261127.py` | 28909 | `8a9afdceca0c7fb291c7c63f18f14943f2fde40802d00915560b8a1e7ad541b6` |
| `topics/visible-flex-new-mechanism/computations/request-r623-current59a4-single-field-geometry-20261127.json` | 14109 | `3ade7784a09551a722c309728a321736bd7caf637848dd7f4c0ef94f58196e3a` |
| `.github/workflows/visible-r623-current59a4-single-field-geometry-20261127.yml` | 7551 | `4ebe3e7de04b091d8b7194e39a27dfe56374eeaee951434ba96f320bdb07ba8a` |

lane `current59a4-one-field-new-all-geometry`；stdin 1713 B，SHA `5987c0ef89ada1c768f5f4d91c656c1829a684252c35cb44998c34c867ae1764`；56个source/旧request/workflow绑定，59条精确sparse路径。
runner先实际pull双仓，核两份README与QUEUE后移除认证，科学仅stdout输出。
