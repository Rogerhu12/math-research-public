# R94 后的局部入口：层 41、辅助素数 47

日期2026-11-12；qc_global。本笔记是进行中的实际局部计算，不登记为新的完整QC结果。R94已给全部全局平移；R77给全部54条特征线的47进高度系数非零，但这两者都不提供局部Poincaré函数或根导数。

## 1. 已完成的准确残差圆盘盘点

`scripts/p41_residue47_inventory.py` 只用标准库，逐个 j∈F47 取一个实际短Weierstrass模型，通过47项Legendre和精确计算椭圆曲线Frobenius迹 t。所有 t²−4·47 在F41中非零，因为24在F41非平方。

除 j=0,1728 外，椭圆曲线的非标量自同构不存在，所以Cartan曲线的粗模F47点恰为Frobenius固定的项链。t≠0时，Frobenius非对合；判别式非平方给唯一项链，平方给零。t=0时，Frobenius为非分裂射影对合，它固定22个项链（自身和R94的21个相邻项链）。这里−47≡35模41非平方。

在j=0,1728处也得到22，而不是不加证明地套用一般纤维。两曲线在47处超奇异，Frobenius共轭CM单位为其逆。对单位商U（阶3或2），固定粗模轨道的数目是
$$\frac1{|U|}\sum_{u\in U}\#\operatorname{Fix}(u\operatorname{Frob};\mathcal V),$$
其中V为820个原始项链。每个uFrob仍满足平方=−47、行列式=47，故仍为同类非分裂对合，各固定22个。公式可直接证明：每个Frob稳定U轨道中，所有v的方程uFrob(v)=v的解数之和恰为|U|，不稳定轨道贡献零。

所得超奇异j是0,9,10,36,44，每个纤维有22个F47点。其余有19个单点纤维：

```
1,5,7,11,12,15,19,24,27,28,30,32,38,39,40,41,43,45,46.
```

其余23个j纤维为空。尖点的Frobenius为47≡6模41，不为±1，故无F47尖点。总数
$$\#X_{\rm ns}^+(41)(\mathbb F_{47})=5(22)+19=129$$
与实际Hecke迹 tr(T47)=−81 给出的47+1−tr(T47)一致。数据见 `scripts/data/p41_residue47_inventory.json`。

这些数据给出全部残差圆盘的有限模描述，但记录的companion矩阵只是Frobenius共轭类；它不是一个已经选好坐标的实际41挠点基。

## 2. 已完成的真实41挠点基及模47⁴提升

可在超奇异曲线E:y²=x³+1/F47开始。其Frobenius满足π²=−47；在E[41]上，−47≡35的乘法阶为40，π的阶准确为80。因此完整E[41]在F_(47^80)定义，任何非零41挠点P和Q=πP自动独立，Frobenius矩阵为
$$\begin{pmatrix}0&-47\\1&0\end{pmatrix}\pmod{41}.$$
独立性的原因是X²+47在F41不可约。还可以用真正Weil配对e41(P,Q)检验它是本原41次单位根。

具体PARI入口为：ffinit(47,80)、ellinit([0,1],ffgen(...))，将随机点乘(47^40−1)/41。E(F_(47^80))的Frobenius是标量47^40，故其指数整除47^40−1；若所得点非零，就有准确41阶。取Q为坐标的47次方。

环境重置后已实际完成两条曲线的计算：CM曲线 $E:y^2=x^3+1$，以及 $E_0:y^2=x^3+x+32$（后者在47模下的 $j=9$）。保存了同一个不可约80次多项式 $f$，两条曲线的实际 $P,Q$ 坐标、配对值和 $t\mapsto\varphi(t)$ 的未分歧Frobenius提升，全部位于
$$R=(\mathbb Z/47^4\mathbb Z)[t]/\widetilde f(t).$$
先通过实际41除法多项式的简单根提升 $x(P)$，继而提升 $y(P)$；$Q=\varphi(P)$。对CM曲线还保存了三次单位 $u$、自同构 $(x,y)\mapsto(ux,y)$ 在基 $(P,Q)$ 上的矩阵，以及对应的实际CM项链标号。生成脚本使用固定随机种子41047，实际有限域配对确定基和CM矩阵，不能由抽象Frobenius矩阵替代。

生成和复核入口：

```
python -B scripts/p41_local47_torsion.py --gp /tmp/pari-2.19.0/gp
python -B scripts/verify_p41_local47_torsion.py
```

生成器的PARI源码是 `scripts/p41_local47_torsion.gp`。数据为 `scripts/data/p41_local47_torsion_certificate.json`，SHA256为 `6384cdce4d6c885f3d2cf706eda2d9af0a8a85d103da42ec6535977aaddc2253`。独立复核器只用Python标准库；它以Rabin判据验证 $f\bmod47$ 不可约，在精确有限环中验证曲线方程、$[41]P=[41]Q=0$、$\varphi(P)=Q$、$\varphi(Q)=[-47]P$，并以实际Miller函数重算
$$e_{41}(P,Q)=-f_{41,P}(Q)/f_{41,Q}(P),$$
确认保存的值恰是本原41次单位根。CM单位的两列作用也在曲线群律中逐一验证。上述全部核验已在环境恢复后通过。

这里 $R$ 不是域，不能把PARI对复合模数多项式的普通逆运算当成可靠单位求逆。生成器和独立复核器均先在 $\mathbb F_{47^{80}}$ 求逆，再用 $b\leftarrow b(2-ab)$ 提升，最后直接检查 $ab=1$；因此所有除法都有实际单位证据。

## 3. 一种较小的Makdisi模型入口

47模41的乘法阶为40；一般普通椭圆曲线的完整41挠点可能要求远大于80的残差扩张。为了构造评价模型，可优先选一个非椭圆超奇异纤维（例如j=9），在单一F_(47^80)上取其820个不同项链作为评价点，而不把所有129个圆盘的完整挠点域混在一起。

需要准确处理权二形式与粗模线丛：权二形式对应K_X+D，次数126、维数73。其乘积生成L(2(K_X+D))（次数252、维数199），再乘得到次数378、维数325的空间；所需正常生成来自126≥2g+1。820个同一非椭圆j纤维中的点多于5·126=630，故可作为这些线性代数表示的分离评价集合。这里尚未计算实际模形式评价矩阵，也尚未证明某个有限精度整基无秩损失。

原始来源：Khuri-Makdisi，*Moduli interpretation of Eisenstein series*，Int. J. Number Theory 8 (2012)，715–748；Mascot，*Moduli-friendly Eisenstein series over the p-adics and the computation of modular Galois representations*，Research in Number Theory 8 (2022)，Paper48。2026的Hashimoto–Lido–Lombardo–Mascot–Parent [预印本](https://arxiv.org/html/2608.10919v1) §§4.1、6.8–6.10只用于识别实现接口，不能把其p13实算当成p41已有结果。

## 4. 仍需真实完成的对象

下一项是生成在项链上的moduli-friendly形式评价和Riemann–Roch空间。随后才有条件计算R94各方向的Mumford/Poincaré截面、全局积分格的坐标及每个残差圆盘上的局部多项式。本文没有用算法存在性、抽象完整平移或Hecke对角横截性替代这些数值对象。
