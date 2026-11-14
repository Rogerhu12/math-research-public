# 固定进程的大素因子、实际完整迹和两个局部符号

日期：2026-11-12。状态：本篇的筛法、整点、高度和局部非零结论已证明；
尚未证明指定点的最底增广层非零。

固定
$$
 E:y^2=x^3-17x,\qquad F=\mathbf Q(\sqrt{-15}),
 \qquad \vartheta=\frac{667}{1000}>\frac23.
 \tag{1}
$$
本篇改变辅助素数的选择次序：先选 $\ell$，再令
$p=P^+(\ell+1)$。得到无穷多个不同的好素数 $p$，及真实的
$$
 \ell+1=pu,\quad v_p(\ell+1)=1,\quad
 Q_{p,\ell}=\operatorname{Tr}_{U}(1+\tau_3)P[\ell],\quad |U|=u,
 \tag{2}
$$
同时满足
$$
 Q_{p,\ell}\ne O,\qquad
 \widehat h(Q_{p,\ell})\ll p^{666/667}\log p=o(p),
 \qquad r_+=r_-=1.
 \tag{3}
$$
这里 $r_\pm$ 是通常 $p$-Selmer 群在 $\lambda\mid\ell$ 的两个
复共轭符号局部像维数。特别地，两个符号都由指定的固定全局点
检测为非零；不是任选一条局部核线。

结论 (3) 不要求 $p$ 在 $F$ 或 $\mathbf Q(i)$ 分裂，也不要求
$E$ 在 $p$ 普通。固定 $q=61$ 的普通盘只用于 R116 的固定
特征零系数非零定理，不能与变化的输入 $p$ 混淆。

## 1. Fouvry 的固定同余类版本与勘误

### 1.1 使用的原文范围

Fouvry（1985），*Théorème de Brun--Titchmarsh; application au
théorème de Fermat*，Invent. Math. **79**, 383--407：

- Theorem 1（印刷 p.383）是数量下界 $\gg x/\log x$，不是只给
  无穷性；移位 $a$ 为任意固定非零整数。
- Theorem 3（pp.384--385）比较通常的平均 Brun--Titchmarsh
  上界与额外附加 $\ell\equiv2\pmod3$ 的版本；后者的主系数
  为前者的一半。
- 印刷 p.386 明确说明，定义中的模 $3$ 条件可以换成另一个
  固定同余条件。证明的具体操作见 pp.397、399：将各乘积变量
  的固定模数剩余类逐一固定；p.400 再次说明同一操作适用于
  后续平均上界。
- §VI，pp.404--406，将这些平均上界代入
  Chebyshev--Hooley 加权和；唯一数值门槛是
  $\int_{1/2}^{\vartheta}C(t)\,dt<1/2$。

原 Theorem 1 的数值 $0.6687$ 有勘误。本篇使用
Fouvry--Tenenbaum（1996），*Répartition statistique des entiers sans
grand facteur premier dans les progressions arithmétiques*，
Proc. London Math. Soc. **72**, 481--514，作者修正版
§3.4、Lemma 3.5 后的说明（该版 p.17）。正确的中段上界是
$$
 C(t)=\frac{14}{12-13t}
       -\max\!\left(0,\log\frac{4(1-t)}{3t}\right),
 \qquad \frac{17}{32}<t\le\frac35.
 \tag{4}
$$
原作者在那里明确将 Theorem 1 的指数修正为 $0.6683$。
下面保留额外余量，使用 (1) 的 $0.667$。

### 1.2 固定模数的准确主项

设 $B\ge1$ 固定。对 $(q,B)=1$ 定义
$$
 \pi_B(x;q)=\#\{\ell\le x:\ell\text{ 素},\
          \ell\equiv-1\pmod B,\ \ell\equiv-1\pmod q\}.
 \tag{5}
$$
在 Fouvry 的附加同余类证明中将模 $3$ 换成模 $B$，主项密度
$1/2$ 换成 $1/\varphi(B)$。这是相同固定剩余类分拆：
每个乘积变量只需在 $(\mathbf Z/B)^\times$ 的有限多个类中
分类；固定 $B$ 不改变任何长度指数，误差常数可以依赖 $B$。
中国剩余定理使 (5) 的主项为
$\operatorname{li}(x)/(\varphi(B)\varphi(q))$。
两个指定类均为 $-1$，与所有固定素因子互素，故没有另一个
兼容性或 gcd 因子。对 $k$ 个乘积变量，允许的固定剩余类
组合有 $\varphi(B)^{k-1}$ 个，合并后正是总密度
$1/\varphi(B)$。

因而 Theorem 3 在各 dyadic 模数段上的准确形状为
$$
 \pi_B(x;q)\le
 \left(\frac{C(\log q/\log x)}{\varphi(B)}+\epsilon\right)
       \frac{x}{\varphi(q)\log x},
 \tag{6}
$$
除去 $O_{A,B}(x^t(\log x)^{-A})$ 个模数 $q\asymp x^t$。
可在使用时将 $\epsilon$ 预先缩小一个固定 $\varphi(B)$ 因子。
这里只主张固定 $B$，没有把该说明升级成对增长模数的一致定理。

为明确说明 (6) 怎样给本题所需移位，考虑
$$
 T_B(x)=\sum_{\substack{\ell\le x\ \ell\equiv-1\ (B)}}
                 \log(\ell+1).
$$
固定进程中的素数定理给 $T_B(x)\sim x/\varphi(B)$。
按 Fouvry §VI 式 (6.2) 展开为素因子加权和，重复素因子及
固定的 $q\mid B$ 只贡献 $o_B(x)$。后者也可直接用固定
$q$ 的幂模数上的 Brun--Titchmarsh 界、再对高幂用平凡计数证明。
于是
$$
 T_B(x)=\sum_{q\text{ 素},\ (q,B)=1}
                  \pi_B(x;q)\log q+o_B(x).
 \tag{7}
$$
Bombieri--Vinogradov 处理 $q\le x^{1/2}$，主项为
$x/(2\varphi(B))+o_B(x)$。平均上界 (6) 和对异常模数的平凡
上界处理 $x^{1/2}<q\le x^\vartheta$。因此
$$
 \sum_{q>x^\vartheta}\pi_B(x;q)\log q
 \ge \frac{x}{\varphi(B)}
       \left(\frac12-\int_{1/2}^{\vartheta}C(t)\,dt-o_B(1)\right).
 \tag{8}
$$
这正是原 §VI 的论证，全部三段都保留相同的
$1/\varphi(B)$；没有把额外同余类的密度丢掉。

### 1.3 一个留有余量的数值证书

Fouvry 的 §VI.1 给
$\int_{1/2}^{17/32}C(t)\,dt\le0.06436$。在 (4) 中舍去
非正项，并在 $3/5\le t\le667/1000$ 使用原 Theorem 3 的
$C(t)=8/(3-t)$，得到
$$
 \int_{1/2}^{667/1000}C(t)\,dt
 \le 0.06436+\frac{14}{13}\log\frac{815}{672}
                      +8\log\frac{2400}{2333}
 <0.498641<\frac12.
 \tag{9}
$$
端点处原证明的任意小 $\epsilon$ 由 (9) 的严格余量吸收。
附带的[纯有理数证书](../scripts/check-fouvry-corrected-integral.py)
使用 $\log x=2\sum_{j\ge0}z^{2j+1}/(2j+1)$、
$z=(x-1)/(x+1)$ 的显式几何尾界认证 (9)；不以浮点近似为输入。

每个 $\ell\le x$ 在 (8) 中的贡献至多 $\log(x+1)$，所以得到
所需固定进程定理：
$$
 \boxed{\#\{\ell\le x:\ell\text{ 素},\ \ell\equiv-1\pmod B,
                  \ P^+(\ell+1)>x^{667/1000}\}
          \gg_B\frac{x}{\log x}.}
 \tag{10}
$$
可以再要求 $\ell>x/(\log x)^2$，因为被删掉的整数总数已经
是 $o(x/\log x)$。这避免从一个累积数量下界未经证明地声称
每个 $[x,2x]$ 都有相同下界。

## 2. 固定进程同时保留全部真实 Heegner 条件

R116 已证明存在固定 $C=60\cdot61^k$ 和 $n_0$，使全部八个
实际最大阶 CM 中心的 $h_{c,n}=n!b_{c,n}$ 在
$C\mid n,n\ge n_0$ 时非零。取一个固定整数
$$
 1020\mid B,\qquad C\mid B,\qquad B\ge n_0.
 \tag{11}
$$
必要时将 $B$ 再乘一个固定正整数即可。由于 (10) 允许任意
固定模数，无需先把 $61^k$ 从进程中消掉。

对 (10) 中的 $\ell$ 令 $p=P^+(\ell+1)$。当 $x$ 充分大时，
$$
 p>x^\vartheta>B,\qquad p^2>\ell+1,
 \quad v_p(\ell+1)=1,
 \quad B\mid u=\frac{\ell+1}{p},
 \quad B\le u\le U_x:=\lceil2x^{1-\vartheta}\rceil.
 \tag{12}
$$
$B\mid u$ 来自 $(p,B)=1$，并非预先限制 $p$ 的剩余类。
由 $1020\mid B$，$\ell$ 在 $F$ 和 $\mathbf Q(i)$ 都惰性，
$a_\ell(E)=0$，与 $2,3,5,17$ 互素。因此 (2) 是 R105、R114
中的原始 Heegner 迹，类群和、全部阶 $u$ 的迹都保留。

R114 的 $\ell$-进 period 及邻点证明只要求上述辅助位条件、
$p\mid\ell+1$、$p\nmid u$；其中没有输入素数 $p$ 的普通性条件。
R116 的固定 $q=61$ 非零进程同样不涉及变化 $p$ 的约化类型。

## 3. 排除真实完整迹的零点

R116 的固定微分系统给非零整数 $J_n$，满足
$$
 \log|J_n|\ll n\log(n+2),\qquad
 Q_{p,\ell}=O\ \Longrightarrow\ \ell\mid J_u
 \quad(C\mid u,u\ge n_0).
 \tag{13}
$$
更强地，$\ell\nmid J_u$ 保证实际首系数 $b_{c,u}$ 是
$\ell$-进单位，并给原规范中的
$v_\ell\log_E([2]Q_{p,\ell})=1/p$。

令所有 $J_n$ 的乘积只遍历 $B\le n\le U_x$、$C\mid n$。
由 (13)，其对数不超过 $O(U_x^2\log U_x)$。因为候选满足
$\log\ell\asymp\log x$，被任何 $J_u$ 整除的候选总数至多
$$
 O\!\left(\frac{U_x^2\log U_x}{\log x}\right)
       =O(x^{666/1000})=o(x/\log x).
 \tag{14}
$$
这里按不同的辅助素数 $\ell$ 计数；$p>x^{1/2}$ 使每个
$\ell+1$ 至多有一个这样的输入素因子，故没有重复预算问题。

## 4. 两个局部符号均非零

### 4.1 正方向

R121 使用两个固定独立点 $P=(-1,4)$、$Q_{\rm MW}=(9,24)$，
构造非零整数 $D_+(U)$，满足
$$
 \log D_+(U)\ll U^2,
 \qquad r_+=0\ \Longrightarrow\ \ell\mid D_+(U_x).
 \tag{15}
$$
实际理由是两点若都落在阶 $u$ 的群 $pE(\mathbf F_\ell)$ 中，
边长 $\lceil\sqrt u\rceil$ 的整数方格产生一个非零整数关系，
其对应非扭全局点约化为 $O$。固定整数点的分母吸收该 $\ell$。
所以正方向坏候选为 $O(U_x^2/\log x)=o(x/\log x)$。

### 4.2 负方向：一个固定秩一点已经足够

取 R103 的固定非扭点
$$
 R'=(121,1144)\in E^{(-15)}(\mathbf Q),\qquad
 E^{(-15)}:y^2=x^3-3825x.
 \tag{16}
$$
对 $n\ge1$，写 $x([n]R')=A_n/B_n$ 为既约有理数，$B_n>0$。
点非扭保证所有这些坐标有定义。典范高度比较给
$$
 \log B_n\ll n^2,
 \qquad D_-(U):=\prod_{1\le n\le U}B_n\ne0,
 \qquad \log D_-(U)\ll U^3.
 \tag{17}
$$
在本篇的 $\ell$，$a_\ell(E)=a_\ell(E^{(-15)})=0$，所以
$\#E^{(-15)}(\mathbf F_\ell)=\ell+1=pu$。若负号局部像
$r_-=0$，则 (16) 的约化落在其阶 $u$ 的 $p$ 倍子群；于是
$$
 [u]\overline {R'}=O,
 \qquad \ell\mid B_u\mid D_-(U_x).
 \tag{18}
$$
从 $E(F_\lambda)$ 到这个二次扭曲的有理剩余点群没有多付一个
条件：$\ell$ 在 $F$ 惰性，负号部分就是该扭曲，且 $2$ 在
$\mathbf F_p$ 中可逆，符号投影与模 $p$ 商相容。

故所有负方向坏候选至多
$$
 O\!\left(\frac{U_x^3}{\log x}\right)
 =O\!\left(\frac{x^{999/1000}}{\log x}\right)
 =o(x/\log x).
 \tag{19}
$$
严格不等式 $3(1-\vartheta)<1$ 正是本篇需要大素因子指数
超过 $2/3$ 的地方。这里无需一个关于固定点约化阶的未证
密度猜想，也无需把原始环类点的非零约化误当成完整迹的非零。

由 (10)、(14)、(15)、(19)，仍有 $\gg_B x/\log x$ 个实际
候选同时使 $Q\ne O$、$r_+=r_-=1$。

## 5. 实际整点的高度改善与无穷多个输入素数

R105 的固定映射给
$\widehat h((1+\tau_3)P[\ell])\ll\log\ell$。
对 (2) 的 $u$ 个真实整数共轭用高度的三角不等式，得到
$$
 \widehat h(Q_{p,\ell})\ll u^2\log\ell.
 \tag{20}
$$
由 $p>x^\vartheta$、$\ell\le x$，
$$
 u\le 2p^{(1-\vartheta)/\vartheta},\qquad
 \log\ell\ll\log p,
 \widehat h(Q_{p,\ell})\ll p^{666/667}\log p=o(p).
 \tag{21}
$$
始终没有把除以 $u$ 或 $\ell+1$ 的有理向量冒充整点。

R107 已证 $E(F^{\rm ab})_{\rm tors}=E[2]$。
由于 $N_{C_p}Q=0$，非零的 $Q$ 必非扭；Baker（2003）
在固定 $F^{\rm ab}$ 上的统一正高度下界遂由 (21) 给
$Q\notin pE(F[\ell])$。

这些输入 $p$ 必无穷，因为 $p>x^\vartheta\to\infty$。
还可保留一个粗数量下界：每个 $p$ 至多对应 $U_x$ 个整数
$u$，故至 $p\le x+1$ 至少得到
$$
 \gg_B \frac{x^\vartheta}{\log x}
 \tag{22}
$$
个不同的成功输入 $p$。这里不声称这些 $p$ 有正密度或
落在预定的分裂同余类。

## 6. 对实际增广格的作用及尚未支付的一层

R119 的 Nekovář 定理对 (2) 给范数一阿贝尔簇
$$
 A=\ker(\operatorname{Res}_{L/F}E\longrightarrow E),
 \quad [L:F]=p,
 \quad \operatorname{rank}_{\mathbf Z}A(F)=p-1,
 \quad \Sha(A/F)\text{ 有限}.
 \tag{23}
$$
这个输入只用实际非零 Heegner 角色投影及 $\mathbf Q(i)$
不包含于 $F[\ell]$，没有普通性假设。
记 $\mathcal O=\mathbf Z_p[\zeta_p]$，
$\delta=\tau^{(p-1)/2}(\tau-1)$，并写
$$
 A(F)\otimes\mathbf Z_p=\mathcal Oe,\qquad
 Q=\delta^a ve,\quad v\in\mathcal O^\times.
 \tag{24}
$$

本篇的 $o(p)$ 高度还使 R109 的二次 Gauss 算子直接作用在
**实际完整迹 $Q$** 上。令
$\mathcal G=\sum_{j=1}^{p-1}(\frac jp)\tau^j$。
它在范数零部分满足 $\mathcal G^\dagger\mathcal G=p$，
在 $\mathcal O$ 中的 $\delta$ 赋值为 $(p-1)/2$。
若 $a\ge(p-1)/2$，则 $\mathcal GQ\in pA(F)$，存在真实整点
$Z=\mathcal GQ/p\in A(F)$；这里从 $p$-进完成回到整群只是在
自由有限生成群中检验模 $p$ 为零。
正定性和 (21) 给
$$
 0<\widehat h(Z)=\widehat h(Q)/p=o(1),
$$
与同一 Baker 下界矛盾。因此
$$
 a\le\frac{p-3}{2}.
 \tag{25}
$$

有限 $\delta$-Selmer 比较只需 $p$ 好且残余表示绝对不可约；
在 $p$ 处所用范数满射来自 $L/F$ 不分歧及好约化，
不需要普通性。对除固定有限集外的本篇输入，R122 的
实际局部符号计算由 $r_-=1$ 得 $a$ 为偶数，由 $r_+=1$ 得
$$
 \Sha(A/F)[p^\infty]\simeq
       \bigoplus_{n\ge1}(\mathcal O/\delta^{2n})^{2m_n},
 \qquad \dim_{\mathbf F_p}\Sha(A/F)[\delta]^+
          =\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
 \tag{26}
$$
R125 已另外完成真正整 Kolyvagin 系统的有限诱导、augmentation
零以及逐精度唯一除 $\delta$；它的 leading term 是实际 $Q$，
不是仍多一个 $\delta$ 的点。因此其已证上界为
$$
 2d_p\le\operatorname{length}_{\mathcal O}\Sha(A/F)[p^\infty]
       \le2a,\qquad
 \boxed{d_p\le a\le\frac{p-3}{2},\quad a\equiv0\pmod2},
 \quad d_p=\dim\Sha(E/\mathbf Q)[p].
 \tag{27}
$$
此处第一不等式来自 (26)，不是从 Kolyvagin 上界反向推出。

即使 (25)--(27) 同时成立，也仍允许 $a=2$ 及相应的有限
$\delta$-Sha 块。本篇支付的是无穷多个实际 $p$ 的两个局部
符号和完整迹的强高度界。主课题仍需该指定 $Q$ 的 $a=0$，
或另一条足够强的整 Selmer 结论。

## 可核来源与现有接口

1. É. Fouvry（1985），Invent. Math. **79**, 383--407，
   Theorems 1、3，p.386 固定同余类说明，§III--VI：
   [DOI](https://doi.org/10.1007/BF01388980)，
   [GDZ 原刊全文](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0079/LOG_0027.pdf)。
   GDZ 的纯文字 OCR 可逐印刷页核查：
   [p.386](https://gdz.sub.uni-goettingen.de/gdzocr/PPN356556735_0079/00000392.xml)、
   [p.400](https://gdz.sub.uni-goettingen.de/gdzocr/PPN356556735_0079/00000406.xml)、
   [p.404](https://gdz.sub.uni-goettingen.de/gdzocr/PPN356556735_0079/00000410.xml)、
   [p.406](https://gdz.sub.uni-goettingen.de/gdzocr/PPN356556735_0079/00000412.xml)。
2. É. Fouvry、G. Tenenbaum（1996），Proc. London Math. Soc.
   **72**, 481--514，§3.4 Lemma 3.5 后的勘误说明：
   [作者修正版全文](https://tenenb.perso.math.cnrs.fr/PPP/RepStatS(x,y).pdf)，
   [DOI](https://doi.org/10.1112/plms/s3-72.3.481)。
   本篇明确采用修正后的 $C(t)$ 和 $0.6683$ 范围。
3. R103 固定负扭曲及 (16)；R105 固定类群和；R114 实际
   period jet；R116 固定进程、非零整数乘积及 $q=61$ 的
   Cornut/ST 证明；R121 固定两个有理点的分母方格。
4. R107 的固定挠群；R109 的实际整 Gauss 算子；R119 的
   Nekovář 全角色有限性；R122 的有限 Sha 分层与局部符号；
   R125 的全好素数整 Kolyvagin 上界。所有接口均使用指定点 (2)，
   没有替换成任意非零范数类。
