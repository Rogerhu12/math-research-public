# M24 R53 真核心：严格反函数、全角三四阶范围与实际入口缓存

日期：2026-11-20。会话：Astra-held10-1b6d88ec-20261120。

## 1. 已支付的结论

本条为新多段 profile 的实际 M24、\(q=.06,\lambda=.002,\tau=1,S=.5,b=.2\) 核心提供独立区间 oracle。它定义并包围 [R53](../results/R53-material-flattening-homotopy-and-positive-domain.md) 的**真数学曲线**：真实 \(2\pi/3\) 周期、原始冻结二进制系数、真实材料反函数和真实积分。原 source 的有限 GL 积分、逆解输出或 lift cache 都没有被当成精确曲线。

实际执行得到全材料角连续界
\[
\kappa<1.984,\quad |\kappa_u|<4.339,\quad |\kappa_{uu}|<117.13,
\tag{1}
\]
\[
|\Gamma'''|<5.298,\qquad |\Gamma''''|<125.035.
\tag{2}
\]
同原 mean1168 节点，真曲线/真初始材料角区间与**实际浮点缓存值**的最大欧氏距离上界为：

| 对象 | 上界 |
| --- | ---: |
| \(\Gamma\) | \(7.235\cdot10^{-13}\) |
| \(\Gamma_u\) | \(2.356\cdot10^{-14}\) |
| \(\Gamma_{uu}\) | \(6.407\cdot10^{-14}\) |
| \(\Gamma_{uuu}\) | \(8.230\cdot10^{-13}\) |
| 完整 lift \(H\) | \(7.275\cdot10^{-13}\) |
| 完整 lift \(H_\psi\) | \(4.265\cdot10^{-14}\) |
| 完整 lift \(H_{\psi\psi}\) | \(1.293\cdot10^{-13}\) |

表中是严格**有限节点**结论，不是源程序浮点函数的连续全角误差定理。式 (1)–(2) 则覆盖整个真实 sector，不是采样最大值。后续含 lift prefix 的连续 metric 可直接使用真区间，免去把 cache 小差再当作近似的步骤。

同一冻结 oracle 另实际导出 2336 个外角节点和全部相邻闭角盒，包含真实 \(2\pi\) 终点及 sector/window 接头。这是连续度量所需的新输入，没有重跑已登记的 1168 均值批次。本条未重跑 BVP、修改 profile、改变均值规则或宣称真 DN/闭面/全族完成。

## 2. 输入、源与接口

实际输入仍是 m3-work/newg-wide-lambda0p002-m24-linear：

    run.json SHA256
    c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a

    physical.npz SHA256
    f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d

三个新源位于 scripts/resume_m3：

| 文件 | SHA256 |
| --- | --- |
| r53_validated_material_core.py | 743ed9b9a38cbc4ec2a3bf5b6d8d340cdc3d5c330bb37626ed453707e7bde197 |
| certify_r53_core_lift_cache.py | 4c3a3c5c6a8226fdf0cd3f423f32f86288f508495f80f9d6f24f24be123e48f4 |
| export_r53_core_angle_boxes.py | 748c56dc2ab0ab343c0719f506cd155ade58ef210c199a5718d36646c7c5afba |

将同实际 model 的 f.exact_lift_core 传入：

    ValidatedMaterialCore(core, mean_kernel_path, interval_kernel_path)

mean kernel 指 certify_r59_fixed_mean_ranges.py，SHA256 ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5；仅复用 outward 区间算术与有余项的三角函数，**不调用桥 profile**。interval kernel 是 R23 的 interval_geometry_kernel.py，SHA256 6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7。

实例 v 的 v.I(lo,hi) 创建实区间；v.point(theta_interval) 返回 F、Ft、Ftt、Fttt、Ftttt，每项为三个 Cartesian 区间，区间 .x 为 lower/upper；另返回 phi、kappa、kappa_u、kappa_uu。导数按材料 \(u\)，不是计算角 \(\psi\)。

该入口用于点或**小材料角盒**；本次接口承诺盒宽不超过 .01，位于本周期或其相邻周期延拓，并按 sector/window 及格点分片。该范围使 Taylor 尾的几何比严格小于一。不要将它不加分片地应用到宽材料角区间。完整 all_angle_curvature_bounds 自行按格点/窗口接头分段。2336 exporter 显式完成这些分片，不依靠调用者默认跨片合法。

## 3. 真核心与严格复条带

取原 24 个冻结 binary64 支持系数 \(c_m\) 为精确有理数，频率 \(m=3,6,\ldots,72\)。旧支持函数及材料映射为
\[
h(\varphi)=1+\sum_m c_m\cos(m\varphi),\quad
\rho(\varphi)=1+\sum_m(1-m^2)c_m\cos(m\varphi),
\]
\[
A(\varphi)=\varphi+\sum_m\frac{(1-m^2)c_m}{m}\sin(m\varphi),\qquad A'=\rho.
\tag{3}
\]
全 24 项绝对和直接给出 \(\rho>.49\)，所以 \(A\) 在整条实轴严格单调，拥有唯一实反函数 \(\varphi(u)\)。

令
\[
B(r)=\sum_m |(1-m^2)c_m|\cosh(mr).
\]
本次严格区间运算给出
\[
B(7/100)\in[.5807816081932013,.5807816081932016]\subset(0,.581).
\tag{4}
\]
在 \(|\operatorname{Im}\varphi|\le r=7/100\) 上 \(|\rho-1|\le B(r)\)。围绕任意实 \(\varphi_0\)，在半径 r 的圆盘边界，
\[
|A(\varphi_0+z)-A(\varphi_0)-z|\le B(r)|z|.
\]
若 \(|w|<r(1-B(r))\)，Rouché 定理比较 z 和上式减 w，给出盘内唯一反解；\(\rho\ne0\) 又保证解析性。因为
\[
R=29/1000<(7/100)(1-.581),
\]
每个实材料角周围的 \(|\Delta u|\le R\) 都有同一解析反函数分支，且
\[
|\varphi(u+\Delta u)-\varphi(u)|<r.
\tag{5}
\]
这不依赖实轴采样，也不搬旧七系数盒。

R53 的 \(S,b,k,\lambda\) 采用实际输入 binary64 的精确有理值。特别是 b 和 k 均为 3602879701896397/18014398509481984；周期是**真实** \(T=2\pi/3\)。原窗给出
\[
\kappa_\lambda=\kappa_0+
\lambda\{\chi(k-\kappa_0)+\beta(1-\chi)\},\qquad \kappa_0=1/\rho.
\tag{6}
\]
\(\beta\) 用真实半周期积分定义。全系数曲率下界仍大于 k，所以 \(\beta\ge0\)；用同一实际 \(\rho\) 绝对和及真实半周期分母，可独立证 \(\beta<3\)。

原九次阶跃 \(W=1-\chi\) 满足 \(W'(t)=630t^4(1-t)^4\)。在以 \(t_0\in[0,1]\) 为中心、半径 \(d=R/.199\) 的复盘，
\[
|t(1-t)|\le1/4+d+d^2,\quad
|W(t)|\le1+630d(1/4+d+d^2)^4.
\]
结合 (4)、\(\lambda<1/499,k<.201,\beta<3\)，每个 analytic 窗片的复曲率满足
\[
|\kappa_\lambda|<5/2.
\tag{7}
\]
切向 \(ie^{i\Phi_\lambda}\) 在对应材料复盘的模因此小于
\[
\exp((5/2)R)<2.
\tag{8}
\]
窗口整体正则性不会变成解析性；高阶 Gaussian 余项只用于已在窗口接头分开的 analytic 片。

## 4. 逆函数 Taylor 与真实 weighted primitive

材料轴按每单位 128 格划分，格点/中心均为精确 dyadic 数，半宽 \(h=1/256\)。每中心先取源逆解为**种子**，再独立计算 (3) 的严格 residual。全局 \(\rho>.49\) 将 residual 变成包含唯一真根的区间，再经区间 Newton 收缩；本次最大真根区间宽小于 \(2.764\cdot10^{-75}\)。源逆解正确性不是证明前提。

写 \(t=(u-u_0)/h\)，构造
\[
\varphi(u)=\varphi_0+\sum_{j=1}^{24}a_jt^j+\text{余项}.
\]
系数来自 \(\varphi_t=h/\rho(\varphi)\)。若
\(E_m(t)=e^{im(\varphi(t)-\varphi_0)}=\sum E_{m,n}t^n\)，则
\[
nE_{m,n}=im\sum_{j=1}^n ja_jE_{m,n-j}.
\]
它生成 \(\rho_n\)，而其逆级数满足
\[
R_0=1/\rho_0,\quad R_n=-\rho_0^{-1}\sum_{j=1}^n\rho_jR_{n-j},
\quad a_{n+1}=hR_n/(n+1).
\tag{9}
\]
所有系数运算均 outward。

由 (5)，普通 \(u-u_0\) Taylor 系数不超过 \(r/R^n\)。令 \(\eta=|u-u_0|/R\)，对截断后的第 \(j=0,1,2,3\) 阶导数，用
\[
\frac{r}{R^j}\frac{(25)_j\eta^{25-j}}
 {1-\frac{26}{26-j}\eta}
\tag{10}
\]
包围余项，\((25)_j\) 为下降阶乘。该式由首项及后继项比值上界的几何级数得出。本条小盒与分片使分母严格为正，代码在实际输入半径上计算尾项，不把“小系数”当作尾项证书。

transition 中的 \(\chi(k-\kappa_0)\) 用严格逆函数多项式的一阶导数乘精确窗多项式，再逐片积分；(10) 的一阶余项乘片长独立加入。窗中点采用两个对称表达式减少抵消，它们仍是同一精确多项式。内窗 primitive 用
\[
kz-\{\varphi(T/2+z)-T/2\}
\]
直接包围，outer primitive 取 transition 终值。本次由真正被包围的积分得到
\[
\beta\in[.7287692832695271,.7287692832696786].
\tag{11}
\]

## 5. 位置积分、字面 GL12 与闭合原点

位置 primitive 使用独立 GL12；格点同时包含逆函数格、真实窗口边界和中点。每个 analytic 片上，(8) 及 Cauchy 导数界给出
\[
|\text{Gauss12 余项}|
\le2\ell\frac{(12!)^4}{25(24!)^2}
 \left(\frac{\ell}{R}\right)^{24}.
\tag{12}
\]
该复向量范数界可由 Hermite 插值的正 Peano 核得到，代码逐片加入。

代码不假定 NumPy 节点/权重恰为真 Gauss 规则。精确有理 Legendre 递推生成 \(P_{12}\)，十二个字面节点各有互不重叠的真根括号；次数为十二，故已穷尽全部真根。以
\[
w_j=\frac{2}{(1-x_j^2)P_{12}'(x_j)^2}
\]
包真权重，再与字面输入逐项比较。本次严格支付
\[
\max|\Delta x_j|\le2^{-53},\qquad
\sum|\Delta w_j|<1.565\cdot10^{-13}.
\]
片长 \(\ell\) 的额外字面规则误差不超过
\[
\frac{\ell}{2}\sum|\Delta w_j|
+\frac{(5/2)\ell^2}{2}\max|\Delta x_j|.
\tag{13}
\]
(12)–(13) 与所有区间算术误差共同保留。

以 \(J(T)=\int_0^Tie^{i\Phi_\lambda(u)}du\)，闭合原点为
\[
\Gamma(0)=J(T)/(e^{iT}-1).
\]
偶曲率与反射对称严格保证其为实数，并非删去一个未经证明的小虚部。独立区间的虚部确包含零，实部为
\[
\Gamma_x(0)\in[1.0606165358624646,1.0606165358628943].
\]
若位置查询盒跨积分接头，以已包围接头值和单位速度差界覆盖全部位置；sector/window/逆函数分片均显式处理。

## 6. 三四阶 jet 与全角范围

真实相位下
\[
\Gamma_u=i\nu,\quad\Gamma_{uu}=-\kappa\nu,\quad
\Gamma_{uuu}=-(\kappa_u+i\kappa^2)\nu,
\]
\[
\Gamma_{uuuu}=(\kappa^3-\kappa_{uu}-3i\kappa\kappa_u)\nu,\qquad
\nu=e^{i\Phi_\lambda}.
\tag{14}
\]
逆函数二、三阶导数给出 \(\kappa_{0,u},\kappa_{0,uu}\)，再用
\[
\kappa_u=(1-\lambda\chi)\kappa_{0,u}
+\lambda W_u(\kappa_0-k+\beta),
\]
\[
\kappa_{uu}=(1-\lambda\chi)\kappa_{0,uu}
+2\lambda W_u\kappa_{0,u}
+\lambda W_{uu}(\kappa_0-k+\beta).
\tag{15}
\]
整个 sector 按真实窗边界与格点逐段包围，含两个单侧极限，实际得到
\[
\kappa\le1.9834503116289222,\quad
|\kappa_u|\le4.338121897502922,\quad
|\kappa_{uu}|\le117.12951034676142,
\]
\[
|\Gamma'''|\le5.297673630526215,\quad
|\Gamma''''|\le125.03410397906096.
\]
这支付了 (1)–(2)，并提供含 lift 角二导 metric 插值的真实输入。

## 7. 已执行的 1168 点与 2336 闭角盒

对实际 literal \(\psi_j\)，用精确冻结
\[
\mathrm{warp\_e}=1080863910568919/2251799813685248,\qquad
\theta_0(\psi)=\psi-\mathrm{warp\_e}\sin(3\psi)/3.
\]
初始 rho、其角导数、基圆和冻结 Fourier 投影均独立区间求值。因此第 1 节 lift 比较同时包含初始角图和投影求值差，不假定 libm 全域误差界。

1168 主证书真实 exit 0，耗时 63.64 秒。小记录：

    geometry-work/newg-m24-r53-core1168-certificate.json
    SHA256 07a97eb8230609e853a343683c44e9fe67e06f70384e53f4717a73623ca97218

严格节点数组仅留 scratch，不入 Git/Release：

    geometry-work/newg-m24-r53-core1168-intervals.npz
    SHA256 f46ee567bf78d8bdac0ceb7c60db92a058f693fd3f532f714125180b911f918c

psi 为 (1168,)。F、Ft、Ftt、Fttt、H、H1、H2 各为 (2,1168,3)，第一轴 lower/upper。H1/H2 是计算角导数，其余为材料导数。F 的最大区间宽 \(1.116\cdot10^{-12}\)；Ft/Ftt/Fttt 最大宽分别小于 \(3.643\cdot10^{-14},8.483\cdot10^{-14},1.242\cdot10^{-12}\)。

随后单独的 exporter 保持前两个源字节不变，仅为新 N=2336 需求构造节点及闭角盒。末 psi_hi 用严格覆盖真实 \(2\pi\) 的 binary 上端，额外微小周期区间也被覆盖。材料映射严格递增，所以两个端点的真 sin 包围可包住整段材料像。每个 sector/window/积分节点的区间两端均插入 exact dyadic 切点；中央微小区间仍单独覆盖，不把近似切点视为真断点。

该新批次真实 exit 0，130.77 秒；共 6332 个材料子盒，每 query 最多 7 片。小记录：

    geometry-work/newg-m24-r53-core2336-angles.json
    SHA256 b5550aaef503363a4f3e75f10649bb1671d829a7d5109321d8261dc23f6ea66c

新数组：

    geometry-work/newg-m24-r53-core2336-angles.npz
    SHA256 0569ce07d1b4721b30c653d4f13db290a4ef5a6f6f4ce03a89ac71c030919234

point_F/point_Ft/point_Ftt/point_Fttt 与 box_F/box_Ft/box_Ftt/box_Fttt 均为 (2,2336,3)。另有 psi、psi_lo、psi_hi、theta_point、theta_box、bindings_json。各 box 包住每个完整 \([\psi_{\rm lo},\psi_{\rm hi}]\) 的真实 jet；point 是节点的严格值。box 最大分量宽度分别小于 .010805、.002999、.010435、.165174；这些宽度是范围信息，不是 metric 误差。

## 8. 仍保留的义务

真核心窗口足有 \(C^6\) 正则性，能够使用 (14)，但这没有把径向五次物理片的全图正则性提高到 \(C^3\)。前半 prefix 的共同 Hermite、精确端点 profile、同 mean1168 真均值以及连续 metric 仍应按各自证明结合。本条没有证明完整闭面、真实非线性尾、固定完整 g 的全族或 held 完成标准。

1168 cache 距离只适用于明确节点；后续应优先直接使用真核心区间。2336 外角规则不改变均值规则。若真实尾联立改变参数或物理场，需要对新输入重新支付实例证书，不能自动继承本条小误差。


## 9. 完整复现命令

先按 M24 前缀记录恢复同一 run/physical。以下命令只生成所需严格输入，不启动 BVP 或真尾。原 1168 节点结果已存在时直接核对绑定并复用；仅新外角网格需要新导出。

~~~bash
HELD10_WORK=/workspace/scratch/1b6d88ecddf3
HELD10_REPO="$HELD10_WORK/math-research-public"
HELD10_SCRIPTS="$HELD10_REPO/topics/visible-flex-held-10pct/scripts/resume_m3"
mkdir -p "$HELD10_WORK/geometry-work"
python "$HELD10_SCRIPTS/certify_r53_core_lift_cache.py" \
  --source-run "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --support-dir "$HELD10_SCRIPTS" \
  --mean-kernel "$HELD10_SCRIPTS/certify_r59_fixed_mean_ranges.py" \
  --interval-kernel "$HELD10_REPO/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py" \
  --nodes 1168 \
  --interval-output "$HELD10_WORK/geometry-work/newg-m24-r53-core1168-intervals.npz" \
  --out "$HELD10_WORK/geometry-work/newg-m24-r53-core1168-certificate.json"
python "$HELD10_SCRIPTS/export_r53_core_angle_boxes.py" \
  --source-run "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --support-dir "$HELD10_SCRIPTS" \
  --mean-kernel "$HELD10_SCRIPTS/certify_r59_fixed_mean_ranges.py" \
  --interval-kernel "$HELD10_REPO/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py" \
  --nodes 2336 \
  --interval-output "$HELD10_WORK/geometry-work/newg-m24-r53-core2336-angles.npz" \
  --out "$HELD10_WORK/geometry-work/newg-m24-r53-core2336-angles.json"
~~~

机器可读的小记录见 [execution JSON](2026-11-20-m24-r53-core-execution.json)。数组只用于后续区间计算，不提交到 Git/Release。

### 实际后续需要的外角细化

后续完整前缀 metric 程序用上述 2336 点/盒作九个径向阶段的严格点探针，得到点处 operator 上界最大约 \(3.12\cdot10^{-7}\)，但角二导包围最大约 \(1.54\)。角插值余项达到 \(1.4\cdot10^{-6}\)，因此仅径向二分不可能据此通过门。这是区间包围不足，不是已证明实际 metric 违反门。

据此，同源正在另导出 4672 外角点/盒；原均值仍为 1168，全部物理参数、实际场和已完成批次保持。新导出完成后才使用其实际 hash，不预记通过或更改本条 2336 的执行身份。
