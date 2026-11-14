# R21 同像集的非保圈材料场：实际有限定义、坐标与连续消费

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

**当前状态：实际 prefix 和 tail 字段均已完整定义并保存；两场完整连续导数界已通过，连续 linear 消费正在执行。**
本文给出字段定义和消费者所用恒等式，不把有限采样误差当成连续证书。
全部 linear residual 的连续消费及 R112 非线性后验完成前，不能登记新的同固定 $g$ 成功族。

## 1. 为什么改用非保圈场

R109 排除了旧 M12/M14 图的保圈重标类，但不排除随角变化的径向材料位移。
直接强制一阶 $E,F$ 误差为零的半测地积分，在 R21 actual M12 的完整 prefix、尾和自身圆领上已实跑：
原采样误差最大约 $1.96653\cdot10^{-8}$，剩余 $G$ 误差却增长到
$4.88807\cdot10^{-6}$，cuff 处还留下非零材料漂移。
这一个积分选择没有被用作新候选。

随后按旋转目标分别对每个物理角 Fourier 模求一个小型带状**线性**最小应变系统，
同时平衡三项误差。第一次 piecewise-linear 全活动带 screen 的 $3072$ 个径向 cell、
$512$ 个角节点给原采样误差 $1.9296933780411876\cdot10^{-8}$，
三次径向加权后的线性误差采样值为 $9.716480021560608\cdot10^{-10}$。
这只是寻找字段的证据；piecewise-linear 字段本身没有被称为 C² 材料微分同胚。

相应已保存报告是
`2026-11-12-fd2d-metric-m12-common-noncircle-gauge-screen-01.json` 和
`2026-11-12-fd2d-metric-m12-common-noncircle-projection-screen-01.json`。
它们的源码和报告没有在本次后续工作中改写。

## 2. 实际字段的有限定义

新的定义使用共享两 jet 的五次 Hermite 径向插值和有限实 Fourier 级数。
对每个节点、两个分量 $p,q$、三个 native 导数阶 $0,1,2$，保存所有
$\cos(3n\psi)$、$\sin(3n\psi)$ 系数（尾上角变量为 $u$）。
所有保存二进数都作为精确有理数解释；各 span 的实际多项式由其两端
同一份值、一阶导、二阶导唯一确定。因此字段在径向接点确实为 C²。
零频 sine 系数准确为零，整个角向周期为 $2\pi/3$。

原型拟合在物理材料角 $u$ 中进行。prefix 的拟合结果在节点上通过

$$
u=\Theta(s,\psi)=\psi-\frac{e(s)}3\sin3\psi
$$

及其链式导数转换为 $\psi$ 中的节点两 jet，再取一个有限 Fourier 级数。
这一步用了浮点插值/FFT，**不宣称是原物理角拟合字段的精确表示**。
转换后保存的二进节点系数和共享 Hermite 规则才定义实际候选；
连续消费者直接验证这个实际候选。
因此转换/截断误差不能通过一个“相同”标签从证明中消失。

实际 prefix 定义在
`2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json`；
有 $1025$ 个径向节点、$512$ 个三重谐波和 $17$ 个独立 SHA 绑定的 gzip shard。
每个 shard 小于 $5$ MB。
保存定义采用 `fd2d-shared-twojet-finite-fourier-material-field-v1` schema。

原 prototype producer `fd2d-metric-c2-material-field-candidate.py` 的真实会话 `34070`
完成了 prefix 的全部拟合、转换、保存和转换后复核。
实际保存字段的同一组 Gauss/角样本上线性误差最大值为

$$
3.076091023608697\cdot10^{-10}.
$$

随后进程在 tail 采样第 $256$ 个 cell 后以 exit $137$ 结束。
工具未提供终止原因；不据此断言是数值不收敛、字段无效或某个确定的内存故障。
该次运行没有 tail 字段或总 production 报告。
prefix 实际文件已完整保存，恢复入口
`fd2d-metric-c2-tail-field-recovery.py` 只重做 tail，不重拟合 prefix。

### 2.1 实际 tail 的独立恢复成功

首个 tail-only 恢复曾做完三轮拟合，但在保存前以 exit 137 结束；
随后低内存入口的一次运行在创建目录时遇到磁盘空间不足，另一次仍在采样进度输出前以 exit 137 结束。
这些运行都没有被解释成实际字段或连续证明。未有工具证据确定 exit 137 的终止原因。

最后的 `fd2d-metric-c2-tail-field-streamfit.py` 使用逐 shard SHA/共享行核查，
只保存点采样需要的导数数组和顺序积分值；它没有保留全部 raw row 的多份副本。
候选采样仍是浮点评估，最终连续消费者独立读取原精确定义。
真实会话 `8847` 以 exit 0 完成，运行约 125.48 秒，峰值 RSS 为 396,296,192 bytes。
唯一一轮线性拟合后立即闭存的实际字段为

`2026-11-12-fd2d-metric-m12-gauge-tail-c2-streamfit-01/tail-field.json`，

SHA256 `936b99bc5153bd9605741f1497cbc52161f3a30df0f8affe77ca7a3ffcb316df`。
它有 1025 个节点、192 个三重 Fourier 模及 17 个 gzip shard；
最大 shard 为 1,164,093 bytes，合计 17,483,649 bytes。
这些实际两 jet 系数定义的字段在原拟合 Gauss/角样本上给

$$
U_{\rm sample}=1.2020292570699756\cdot10^{-9}.
$$

采样 Fourier 表中未参与拟合的模式按完整绝对系数和另外计费，
该采样计费为 $3.3601170000778274\cdot10^{-21}$。
这仍只是对保存定义的有限样本复核，不控制样本间的径向/角向变化。
同目录 `production.json` 绑定两份实际字段、所有原图输入和 producer；
`weights-next.npz.gz` 留存下一轮加权入口，但当前实际候选就是已保存的一轮结果。
前缀字段在这次恢复中没有重拟合或修改。

## 3. native、冻结目标与物理弧长的明确区分

### 3.1 Prefix 后验采用冻结目标的 native 坐标

prefix actual field 定义在原保存的 $s,\psi$ 上，材料角仍是上述固定的 $u=\Theta(s,\psi)$。
令其材料分量为 $p_n(s,u),q_n(s,u)$，实际变换在该图中定义为

$$
\Phi_n(s,u)=(s+p_n(s,u),\ u+q_n(s,u)).
\tag{1}
$$

prefix 连续 linear consumer 使用自己原有的冻结目标

$$
g_0=ds^2+a_0(s)^2du^2.
\tag{2}
$$

所以 R112 的 prefix 非线性后验也必须对 (1)、(2) 使用同一 native 坐标。
最后再用原 exact bridge 证书的
`relative_target_metric_difference_upper = 3.319321476658082e-13`
转移到 R21 的原固定目标 $g$。
这个转移是两份**固定目标**在同一材料图中的点态比较，
不会因实际嵌入从 $X$ 改成 $X\circ\Phi_n$ 而失效。

为了与全局公共材料面的物理弧长记号一致，若
$\lambda=S/L_{\rm exact}$、$\sigma=s/\lambda$，则同一个变换的物理径向分量为

$$
p_{\rm phys}(\sigma,u)=\lambda^{-1}p_n(\lambda\sigma,u),
\qquad q_{\rm phys}(\sigma,u)=q_n(\lambda\sigma,u).
\tag{3}
$$

特别地

$$
(p_{\rm phys})_\sigma=(p_n)_s,\quad
(p_{\rm phys})_u=(p_n)_u/\lambda,\quad
(p_{\rm phys})_{\sigma\sigma}=\lambda(p_n)_{ss},
$$
$$
(p_{\rm phys})_{\sigma u}=(p_n)_{su},\quad
(p_{\rm phys})_{uu}=(p_n)_{uu}/\lambda,
$$
$$
(q_{\rm phys})_\sigma=\lambda(q_n)_s,\quad
(q_{\rm phys})_{\sigma\sigma}=\lambda^2(q_n)_{ss},\quad
(q_{\rm phys})_{\sigma u}=\lambda(q_n)_{su}.
\tag{4}
$$

导数消费者先严格算出 native 材料导数，再把所有界统一乘
$L_*^2\ge1$，其中 $L_*\ge\max\{\lambda,1/\lambda\}$ 由同一个 exact bridge 区间给出。
故报告的数值**同时**上界 native 分量导数和 (3) 的物理分量导数。
prefix posterior 仍明确使用 native 对象；这不是把对一个对象的线性误差和另一个对象的导数混合。

### 3.2 Tail 使用真实物理弧长

tail 保存字段以实际物理半径 $r$ 和材料角 $u$ 写成有限 Fourier/Hermite 函数
$p_T(r,u),q_T(r,u)$，但 $p_T$ 的分量单位是物理 meridian 弧长 $\sigma$。
定义

$$
\sigma=L_{\rm exact}+\int_r^c\sqrt{1+w(t)^2}\,dt,
\qquad k=\frac{dr}{d\sigma}=-\frac1{\sqrt{1+w^2}}.
\tag{5}
$$

tail 变换是在 $(\sigma,u)$ 中作
$(\sigma,u)\mapsto(\sigma+p_T(r(\sigma),u),u+q_T(r(\sigma),u))$。
需要新半径时，使用 (5) 的严格单调反函数定义；不把某个显示用的弧长累加数组当成物理背景。

因此

$$
p_\sigma=k p_r,\quad p_{\sigma u}=k p_{ru},\quad
p_{\sigma\sigma}=k^2p_{rr}+kk_rp_r,
\tag{6}
$$

$q$ 同理。已有目标 K6 给
$|k|\le1$、$|kk_r|=|ww_r|/(1+w^2)^2\le6$。
这里不需要 $w_{rr}$，也不需要曲面的三阶全局导数。

实际 tail 字段的 native interval 取精确二进 $.4$ 到精确二进 $.6$；
把 $r\le.4+.002$ 及 $r\ge.6-.01$ 的所有网格节点完整两 jet 设为零。
准确的函数零带一直延续到相邻的最后一个连续零节点；
不能把节点选择阈值直接当成同宽的连续零带。
实际支撑包围由完整字段报告的 `field_support_native_enclosure` 给出。
尾内侧全部延拓为零，尤其在 $r\le.4$ 恒等为零。
原图在整个 cuff 到 exact binary $.4$ 上已经由自身完整旧证书给

$$
\|g^{-1/2}(X^*e-g)g^{-1/2}\|_{op}
\le1.1313778765583975\cdot10^{-9}.
\tag{7}
$$

这是重组旧已证行的最大值，没有删掉跨分界的行或用 displayed radius 判断覆盖。
见 `2026-11-12-fd2d-metric-m12-tail-gauge-support-regions.json`。
因此只需在外侧重新消费真正改变的 linear residual；深尾、自身 R6 collar 和帽保持原图。

### 3.3 接口与相位

prefix 和 tail 在 common cut 两侧都有整段零字段，所以 (1) 与 (5) 的两种参数实现
通过恒等映射准确拼接，不需要匹配两个非零字段的近似端迹。
中央镜像直接强制每个 Fourier 系数满足
$p(0)=p_{ss}(0)=q_s(0)=0$，以 $p$ 奇、$q$ 偶延拓得到 C² 字段。
这里还使用原精确 clamped 角图的 $e_s(0)=0$，所以 $b(0)=0$；
$p(0,\psi)$ 恒零也使其全部角导在该圈为零。
将这些准确恒等代入 (8)，得到物理材料角下同样的
$p(0)=p_{ss}^{\rm mat}(0)=q_s^{\rm mat}(0)=0$，而非只核 native jet 后略过图册转换。
帽邻域字段为零，不触及角坐标的极点。

若连续导数界给 $\|Dv\|<1$，可把零带外延拓的周期 lift 写成
$\mathrm{Id}+v$；其与恒等的全局 Lipschitz 差小于一。
距离下界及 Banach 不动点论证给全局双射，局部逆函数定理给 C² 逆。
这随后下降到圆柱并在帽上以恒等拼成整个 $S^2$ 的 C² 微分同胚。

新的活动族须按 R112 写成
$Y_\alpha=R_\alpha(X_0\circ\Phi)\circ\tau_{-\alpha}$，固定帽另取原定义。
不能改写成 $X_\alpha\circ\Phi$ 来假定 $\Phi$ 与材料旋转可交换。
一旦 $\Phi$ 是全局微分同胚，每个 $Y_\alpha$ 的像集准确等于对应旧 M12 像集，
所以 reach、直径、握持 Hausdorff、含反射不全等和已有像集网格均直接属于同一组像集。
度量仍需新的实际连续/非线性证明。

## 4. 已完成的实际 prefix 连续导数界

`fd2d-metric-material-field-bounds.py` 使用全部保存谐波和每个实际 span 的 Bernstein 凸包。
它没有采用 Fourier 截断外的“数值够小”舍弃规则。
材料图 $e,e_s,e_{ss}$ 则从原定义的精确有理 clamped spline 和 quintic cutoff 包围，
没有对一个 uniform remainder 作微分。

其真实会话 `70280` 正常退出，报告
`2026-11-12-fd2d-metric-m12-prefix-field-bounds-01.json` 给

| 量 | 连续上界 |
|---|---:|
| $|p|$ | $1.1362026047307063\cdot10^{-11}$ |
| $|q|$ | $2.1748397698072635\cdot10^{-11}$ |
| $\|Dv\|_{op}$ | $7.676502902047499\cdot10^{-9}$ |
| $\|D^2v\|$ | $6.283364928357972\cdot10^{-6}$ |

同一报告还包含全部十二个分量导数界、字段/shard SHA、精确桥比例和完整径向/角向覆盖。
它的 `global_field_components_present=false` 正确保留只有 prefix 的范围。
报告中 prefix 的 `exact_zero_endpoint_jets_verified` 指 **cut 零延拓端**；
中央端使用另列的镜像身份，$q(0)$ 本来允许非零，不把该标记解释为中央字段也全零。

对标量 $f(s,\psi)$，设 $\rho=1-e\cos3\psi$、$\nu=-e_s\sin3\psi/3$、$b=\nu/\rho$。
消费者所用材料导数恒等式是

$$
f_s^{\rm mat}=f_s-bf_\psi,\qquad f_u=f_\psi/\rho,
$$
$$
f_{ss}^{\rm mat}=f_{ss}-2bf_{s\psi}+b^2f_{\psi\psi}
 -(b_s-bb_\psi)f_\psi,
$$
$$
f_{su}=\frac{f_{s\psi}-bf_{\psi\psi}-b_\psi f_\psi}{\rho},\qquad
f_{uu}=\frac{f_{\psi\psi}}{\rho^2}-\frac{\rho_\psi f_\psi}{\rho^3}.
\tag{8}
$$

所有分母有原固定图册的严格正下界。
各坐标项的三角界再作有限维 Frobenius 上界，给上述 $Dv,D^2v$ 数值。

### 4.1 两场合并的完整实际连续导数证书

同一消费者随后以两份实际字段共同输入，真实会话 `98753` 以 exit 0 完成，
报告为 `2026-11-12-fd2d-metric-m12-global-field-bounds-01.json`。
此处 `global_field_components_present=true`，完整有限角模和 native 径向区间都已覆盖。
前缀按 (8) 转材料导数并按 (4) 保守同时覆盖两种弧长约定；尾按 (6) 转物理弧长。
两场导数的逐项最大值为：

| 导数 | 连续上界 |
|---|---:|
| $|p|$ | $1.5348355764193366\cdot10^{-11}$ |
| $|q|$ | $2.1748397698072635\cdot10^{-11}$ |
| $|p_s|$ | $1.3721433762718312\cdot10^{-8}$ |
| $|p_u|$ | $4.986911388057387\cdot10^{-9}$ |
| $|q_s|$ | $2.64074477661233\cdot10^{-9}$ |
| $|q_u|$ | $4.48015017480398\cdot10^{-9}$ |
| $|p_{ss}|$ | $1.9127765043363293\cdot10^{-4}$ |
| $|p_{su}|$ | $1.7426583148867787\cdot10^{-6}$ |
| $|p_{uu}|$ | $3.5407158302633687\cdot10^{-6}$ |
| $|q_{ss}|$ | $1.1099846320818066\cdot10^{-5}$ |
| $|q_{su}|$ | $1.3471113020612167\cdot10^{-6}$ |
| $|q_{uu}|$ | $2.209996158494172\cdot10^{-6}$ |

以欧氏坐标 Frobenius 上界组合后，

$$
\|Dv\|\le1.5498138864425113\cdot10^{-8},\qquad
\|D^2v\|\le1.9167021163731551\cdot10^{-4}.
$$

这些是实际字段的连续界，故 §3.3 的全局 C² 微分同胚结论已可应用。
这份报告本身仍未计算 linear residual，也未证明最终度量误差。
不能仅凭它的四个充分 field box 为 true，就把 R112 的完整后验误读为已通过。

## 5. 连续 linear residual 的有限多项式公式

prefix 中原实际 Gram 写为 $E,F,G$，冻结 target 的适应图 Gram 是
$1+a^2\nu^2,a^2\nu\rho,a^2\rho^2$。
令

$$
D=E-(1+a^2\nu^2),\quad B=F-a^2\nu\rho,\quad N=G-a^2\rho^2.
$$

实际字段的 native 导数和角导数均来自其保存多项式。
相对于 $ds^2+a^2du^2$ 的线性误差三个分子为

$$
R=\rho^2D-2\nu\rho B+\nu^2N+2\rho^2p_s-2\nu\rho p_\psi,
\tag{9}
$$
$$
T=\rho B-\nu N+\rho p_\psi+a^2\rho^2q_s-a^2\nu\rho q_\psi,
\tag{10}
$$
$$
U=N+2a^2\rho q_\psi.
\tag{11}
$$

归一矩阵的分量为
$R/\rho^2,T/(a\rho^2),U/(a^2\rho^2)+2a'p/a$。
最后一个小项可单独用 $|a'|\le1$ 包围，避免对 radius packet 余项作导数，
也避免把已能准确相消的 $\rho^2$ 又丢进一个粗分母。
这些公式对实际字段的 cosine/sine 两部分都应用；不把浮点转换后的小 parity 系数默认为零。

所有分子都是径向多项式和有限 Fourier 级数。
在双方/目标/材料图的精确节点并集上，先形成这些系数差，再用径向 Bernstein 凸包和
覆盖完整圆周的严格三角函数弧区间得到实际全域上界。
三角端点由原 Machin/Taylor 区间程序计算；不是角节点采样。
宽 Fourier 字段乘窄 target 的卷积可等价写成 Toeplitz 径向区间矩阵乘法；
其每个系数仍是同一个有限卷积，沿用原后端向外舍入的矩阵乘法预算。

tail 用原实际有限尾的 residual 分子 $E_r,F_r,G_r$（它们不是导数记号）。
因为整尾高度反射且 $dr/d\sigma=k<0$，相应 linear 分子是

$$
R_T=E_r+2k(1+w^2)p_r,\quad
T_T=-F_r+\sqrt{1+w^2}p_u-r^2q_r,
$$
$$
U_T=G_r+2rk p+2r^2q_u,
\tag{12}
$$

分别除以 $1+w^2,r\sqrt{1+w^2},r^2$。
这里原尾的 $F_r$ 符号不能沿用到物理 $\sigma$ 而漏掉负号。
同一 actual tail 的背景包给每个精确区间的 $w$；
$k$ 和平方根可在该区间以严格常区间参与系数运算。
本式仅重估改变区域的 linear residual，深尾仍用 (7)。

## 6. Actual closed-map manifest 与材料点求值

`scripts/fd2d-metric-repaired-closed-map.py` 的 `make` 入口已实际生成
`2026-11-12-fd2d-metric-m12-repaired-closed-map.json`。
它绑定原 M12 完整 common prefix、实际尾、原目标/精确桥、原整体和更紧直径证书、
两份实际字段、完整连续导数证书与现有三个相位网格。
帽使用原精确二进 cuff 半径
$2702159776422297/18014398509481984$，而不是把显示的 $.15$ 重新当作一个不同精确边界。
只有上帽保留 R16 的三个固定凸起；上下帽的材料变换都是恒等。

这个 manifest 的数学对象已经定义，其状态同时明确写为
`ACTUAL_C2_SAME_IMAGE_FAMILY_DEFINED__NEW_METRIC_POSTERIOR_SEPARATE`。
其中列出的实际字段/同像集定理，不以尚未结束的连续 linear 计算冒充最终度量证书。
旧网格展示相同的像集，但原顶点的材料标签没有被伪称为新 $\Phi$ 的标签。

`phi` 入口输入半图上的非负坐标、材料角和相位，返回供原图计算器使用的点坐标。
例如从本题目录运行：

```sh
python scripts/fd2d-metric-repaired-closed-map.py phi \
  --manifest notes/2026-11-12-fd2d-metric-m12-repaired-closed-map.json \
  --region prefix --coordinate 0.8 --u 0.4 --t 1/4 --side upper
```

prefix 默认输入 native $s$；加 `--prefix-units physical` 则输入正向物理 $\sigma$，
数值查询使用精确桥区间的中点代表 $\lambda$，数学定义仍取原唯一精确桥。
上下半图用同一个非负输入坐标，`--side lower` 负责径向材料分量的奇延拓和原图的 z 镜像。
输出 `mapped_native_s,mapped_material_u,mapped_native_psi`，然后对原 $X_0$ 的点作所列 ambient rotation。
这里先用 $u-\alpha$ 求字段，再作 $\Phi$，没有错误地交换这两个操作。

尾输入 `--region tail --coordinate 0.5` 的 coordinate 是真实半径 $r$。
程序从原全部 raw shard 的精确归一化增量重建半径网格，只用原同背景包的数值代表来求

$$\int_{r'}^r\sqrt{1+w(z)^2}\,dz=p_T(r,u-\alpha).$$

计算在很小的 $\Delta r=r'-r$ 上作单调二分，避免用两个 O(1) 的累计弧长相减。
返回 `mapped_radius,mapped_material_u`，仍由原实际 $X_0$ 计算器和 ambient rotation 给空间点。
这套浮点求值没有替换严格连续消费者的包围，也不宣称数值代表的积分残差就是对原精确 $w$ 的误差证书。

`demo` 真实会话 `58029` 正常结束，报告
`2026-11-12-fd2d-metric-m12-material-evaluator-demo.json` 保存 42 个查询：
三个相位、上下半图、prefix 中心/内部/cut、tail 内零带/采样误差峰附近/cut 和固定帽。
帽恒等及上下 p 奇/q 偶均在输出中保持。
数值角逆残差最大为 $5.421010862427522\cdot10^{-20}$，
所选背景数值代表的相对弧长逆残差最大为 $7.888609052210118\cdot10^{-31}$。
这些数值只说明点求值程序确实跑通；全域证书仍是前述独立的连续计算和 R112 后验。

## 7. 完成门仍需的实际输入

R112 已有只用旧图误差、实际 $v,Dv,D^2v$ 和目标一二导的非线性后验；
不需要另构造一个 $E$ 导数证书。
本分工当前要把真实有限字段的连续 linear 上界与上述连续导数界一起交给该消费者。
prefix 的目标身份是 (2)，tail 是原物理目标；切口零带保证每个被移动的点和像点留在同一图中。
最终合并各片的局部后验，再只对 prefix 支付原桥目标转移。
该过程不要求人为把两张在零带外分别使用的分析坐标变成一张近似“统一弧长表”。

在这些实际报告齐备前，仍是候选，不是 README 完成结论。
