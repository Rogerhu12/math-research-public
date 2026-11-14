# R154：原始 coast 到上下完整固定帽的全相位交叉法球

2026-11-12，fd2d geometry。**完整证明及实际连续计算均已完成。**

对 [R151](R151-actual-coast-complete-self-normal-balls.md) 的同一个原始 $\delta=0$ coast、它的上下镜像，以及 [R121](R121-corner-fixed-caps-and-a-wider-active-window.md) 的上下完整固定帽，本结果支付所有 coast–帽点对的正常球。固定帽使用真正的平环、喉及完整凸体表面，未以几个标记点代替帽。

在 R121 原允许高度窗 $9/10\le Z\le z_c^{\rm corner}$ 内，不增加任何新高度约束。实际 cut 高度仍必须由真正的前缀重建和刚体接合得到；本文不将背景高度替代为实际 $Z$，也不声称未知前缀、尾或接缝已经完成。

## 1. 精确对象及结论

记
$$
\rho=\frac{17}{125},\qquad a_c=\frac8{25},\qquad a=\frac3{10},\qquad\lambda=\frac1{100}.
\tag{1}
$$
上 coast $S$ 仍是 R145、R151 保存的完整 Cartesian 有限 Fourier 定义
$$
F(\phi,\tau)=X(\phi)+\tau W(\phi)
\left(e_1(\phi)-\frac{m(\phi)}{n(\phi)}e_2(\phi)\right),
\quad 0\le\tau\le1,\quad\phi\in\mathbb R/(2\pi\mathbb Z).
\tag{2}
$$
令 $S^-$ 为关于 $z=0$ 的反射片，$K_Z^+$、$K_Z^-$ 为 R121 中 cuff 平面位于 $z=Z$、$z=-Z$ 的上下完整帽。

对任何 $Z\ge9/10$，并对上、下 coast 分别施加任意绕 z 轴的旋转，均有
$$
\boxed{\operatorname{dist}\bigl(S\cup S^-,\ K_Z^+\cup K_Z^-\bigr)
>\frac{73}{250}=.292>2\rho=.272.}
\tag{3}
$$
这里平移帽的定义仍为 R121 的同一显式公式；要同时使用 R121 的直径、held 和标记预算，实际 $Z$ 还须处于其原允许上界 $z_c^{\rm corner}$ 以下。

特别地，对任何 coast 点 $P$、任一完整帽点 $Q$，以及两端实际单位法向和两个法球符号，均有严格余量
$$
\boxed{|Q-P|^2-2s\rho N_P\cdot(Q-P)>\frac{73}{12500}=.00584,
\qquad s=\pm1,}
\tag{4}
$$
交换 P、Q 后同样成立。这是全部点对、全部相位的交叉排除。

## 2. 原 coast 的有证位置输入

已有完整位置包在所有角、所有径向上给出 $z>14/25$。本次直接从同一包的准确二进制端点读取还得到
$$
\frac{14}{25}<z<\frac{22}{25}=.88.
\tag{5}
$$
最大已证上端点约 $.8790399387723837$。径向位置对 $\tau$ 仿射，所以每个角盒的入口、出口 z 范围的并已经覆盖整条 ruling。

该位置包是
`notes/2026-11-12-fd2d-k0-ruling-position-certificate-01.json`，SHA256
`b941b2bff3cb3f6223580632948f9095a5406369278bd7071b2c4f993900ed6e`。
同一个入口实体 SHA256 为
`ed69b9a6599ef75f36f2d5bc094d152d993baeb078f4852a392648b85f6c9c3a`；
同一个物理候选 SHA256 为
`7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
本次没有更换它们的 $g$、角坐标或位置。

## 3. 到整个 cuff 半无限柱的严格距离

定义实心半无限柱
$$
C_Z=\{(x,y,z):\sqrt{x^2+y^2}\le a_c,\ z\ge Z\}.
\tag{6}
$$
若 $r=\sqrt{x^2+y^2}$，则对任一点 $P=(x,y,z)$，
$$
\operatorname{dist}(P,C_Z)^2
=\bigl(\max(r-a_c,0)\bigr)^2+igl(\max(Z-z,0)\bigr)^2.
\tag{7}
$$
证明是两个正交坐标因子的最近点分别求解：水平最近点为圆盘内原点径向的裁剪，竖直最近点为 $\max(z,Z)$；平方距离相加。

程序以128个闭角区间覆盖完整圆周，每个角盒再用16个完整 $\tau$ 条带覆盖 $[0,1]$。每一盒均以 R151 冻结位置 reader 的真 Taylor jets 和全部有限 Fourier 尾包含 (2) 的坐标，未只计算节点。对一盒设
$$
r\ge r_*,\qquad z\le z^*,\qquad h_*:=\max(r_*-a_c,0).
$$
于是 (7) 的可靠下界为
$$
h_*^2+\max(Z-z^*,0)^2.
\tag{8}
$$
这里的 $z^*$ 还与第2节已经完成的全域上界取较小者；两者都是同一个实际 F 的界，故这一相交只收紧包含。

在全部2048个连续盒上，本次实际计算证明
$$
\boxed{\operatorname{dist}(S,C_{9/10})^2
\ge .1523843608748449\ldots>\left(\frac{39}{100}\right)^2.}
\tag{9}
$$
省略号处的严格数值由保存的二进制端点给出，不以这行显示小数作向外舍入。因此
$\operatorname{dist}(S,C_{9/10})>.39$。

实际执行 session8851 / chunk `d012ad` / 自然 exit0，9.982968852秒；完整128角盒、2048径向条带，无未决，没有使用 Cartesian 对称来缩短圆周。

源码 `scripts/fd2d_k0_coast_caps_cylinder_certificate.py`，SHA256
`e815cb5f7e4e857479f14ccf3f51c1efb254d5ce0a7ae489ddec4795b7ddc815`。
报告 `notes/2026-11-12-fd2d-k0-coast-caps-cylinder-certificate-01.json.gz`，SHA256
`dab733bf7f47c55bb7ef4356e91025873a3d0479d413546e1299a8846204e3bd`。

这个计算也保留了可复用的高度充分条件。若一个盒的 $h_*>2\rho$，它对任意 Z 已自动分离；否则只需
$$
Z>z^*+\sqrt{(2\rho)^2-h_*^2}.
\tag{10}
$$
全部盒的右端有证上界约 $.6917426257173789$，严格小于 $3459/5000=.6918$。因此仅对半无限柱而言，$Z\ge.6918$ 已经足够。本结果在完整帽上仍采用 R121 的原 $Z\ge.9$ 窗，没有把这个柱域阈值自动当作所有帽和 held 条件的新窗口。

## 4. 完整上帽的准确分解

R121 的上帽由下面两个集合组成。

第一部分是平环和光滑喉。平环为 $a\le r\le a_c$、$z=Z$；喉的准确母线是
$$
r(\theta)=a-\rho\sin\theta-2\lambda\rho\sqrt{\sin\theta},
$$
$$
z(\theta)=Z+\rho(1-\cos\theta)
+\lambda\rho\int_0^\theta\sqrt{\sin t}\,dt,
\qquad0\le\theta\le\pi.
\tag{11}
$$
因而全部 $r\le a<a_c$、$z\ge Z$。平环和喉都在 $C_Z$ 中。
若 $Z\ge.9$，则 $C_Z\subset C_{.9}$，由 (9)，
$$
\operatorname{dist}(S,\text{平环或喉})>.39>.292.
\tag{12}
$$

第二部分为完整凸体表面除接合圆孔的部分。设
$I=\int_0^\pi\sqrt{\sin t}\,dt>0$。R121 中
$$
z_c^{\rm corner}=h-\epsilon-3\rho-\rho\lambda I,
\qquad d=z_c^{\rm corner}-Z.
$$
帽的凸体在平移前全部位于 $z\ge h-\epsilon-\rho$，平移 $-d e_z$ 后全部位于
$$
z\ge h-\epsilon-\rho-d=Z+2\rho+\rho\lambda I>Z+2\rho.
\tag{13}
$$
这是整个真实凸体的高度界，不仅是标记点的界。去掉接合圆孔只缩小集合，不改变这个包含。结合 (5)、$Z\ge.9$ 和 (13)，所有上 coast–凸体点对的竖直距离严格大于
$$
\frac9{10}+2\frac{17}{125}-\frac{22}{25}
=\frac{73}{250}=.292.
\tag{14}
$$
平环、喉与这个凸体部分穷尽完整上帽；(12)、(14) 遂付清上 coast 与同侧完整帽的所有点对。

## 5. 下帽、相位和法球余量

完整下帽为上帽的反射，故其全部点满足 $z\le-Z$。由 (5)，上 coast 到任何下帽点的距离大于
$$
\frac{14}{25}+\frac9{10}=\frac{73}{50}=1.46>.292.
\tag{15}
$$
反射得到下 coast 与两帽的同样结论，证明 (3)。

绕 z 轴的任意旋转保持 r 和 z，因此 (5)、(7)–(15) 对任意 coast 相位仍成立。帽保持不动也不影响这两个位置量的比较。这里不需要离散时间网格，也不假定帽随 coast 旋转；上、下 coast 的两个相位甚至可以独立选择。

最后令 $d=|Q-P|$。对任一实际单位法向、任一符号 s，由 Cauchy–Schwarz，
$$
|Q-P|^2-2s\rho N_P\cdot(Q-P)
\ge d(d-2\rho).
$$
函数 $d(d-2\rho)$ 在 $d>2\rho$ 上严格递增，由 (3)，
$$
d(d-2\rho)>
\frac{73}{250}\left(\frac{73}{250}-\frac{34}{125}\right)
=\frac{73}{12500},
$$
得到 (4)。同一距离界同样适用于帽端法向，故四种交叉正常球全部支付。

## 6. 实际消费与可用范围

`scripts/fd2d_k0_coast_caps_cross_normal_balls.py` 直接核对上述全域位置、柱域报告和已完成 R151 的输入身份，并用准确区间/有理常数核对 $.39$、$.88$、$.292$ 与 $.00584$ 的严格余量。实际 session15776 / chunk `6f9909` / 自然 exit0，.165359195秒。

源码 SHA256
`754e22b4bac3a212d01af833d5dda52a25bf63f4d4f88849b961e783c92ea4d0`。
最终报告 `notes/2026-11-12-fd2d-k0-coast-caps-cross-normal-balls-01.json`，SHA256
`8380d094be773d64437e328c107e35482bf6c240e8576f06d1407036ed52fdfb`。

结合 R151，可直接使用原始上下 coast 的自身、彼此，以及它们到上下完整固定帽的全部法球检查。要把这些片真正组成本课题的闭曲面，仍需同一个实际核给出其余前缀、尾、固定 cuff 的准确位置和两 jet；真实 cuff 高度须落在 R121 允许窗内，且剩余片之间的正常球须另付。本文没有把已冻结原片的证书移给改变后的非零 $\delta$ 场，也没有因完成这一块点对检查而宣称整个强目标已经完成。
