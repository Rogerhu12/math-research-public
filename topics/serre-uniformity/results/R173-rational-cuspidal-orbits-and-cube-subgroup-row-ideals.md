# R173：有理尖点型轨道与三次子群的指定行理想

日期：2026-11-13。

**状态：已证明的有理轨道增强与整行理想恒等式。** 本文在 R166、R169、R172 的同一个实际小惯性分支中工作。一个满足 R172 非零中心值条件的完整有理轨道，已经能提供两个三次角色方向及所有原始 $\theta$ 共轭的指定尖点行；不必为每个方向另找中心值。两条方向的整行理想之和，恰为 $C^3$ 的一个秩二等型投影的整行理想。

这里的增强没有移动实际尖点、实际加性角色或实际剩余素理想。它仍以至少一个实际尖点型中心值非零为前提，也尚未证明新的指定行理想恒为单位。

## 1. 设置与完整结论

设 $p>37$，处于 R166 的完整非分裂 Cartan 正规化子、小惯性分支。置
$$
\overline C=C/\mathbb F_p^\times,
\qquad |\overline C|=p+1=3d,
\qquad 3\nmid d,
\qquad d>4.
\tag{173.1}
$$
令 $H=\overline C^3$，其阶为 $d$。取阶为 $d$ 的字符 $\theta$ 及阶三字符 $\vartheta$。$\theta$ 在 $\overline C$ 的阶三子群上平凡，而 $\vartheta$ 在 $H$ 上平凡。记
$$\theta_u=\theta^u\quad(u\in(\mathbb Z/d\mathbb Z)^\times).$$

取 R166 的一个实际非 CM 新形式 $f$，其有限尖点型为 $R_\theta$。假设对于
$$\Xi=(\theta\vartheta)\circ\lambda$$
有
$$L\!\left(\tfrac12,\pi_{f,K}\otimes\Xi\right)\ne0.\tag{173.2}$$
用 $\vartheta^{-1}$ 开始完全一样。由 R172，完整有理兼容系统轨道在每个配对分支上的实际非零商 $B_\alpha$ 都满足 $B_\alpha(\mathbb Q)$ 有限。

在一个实际尖点采用 R169 的同一 Cartan 嵌入、幺幂群 $u_x$、对角元 $d_s$、原始加性角色 $\psi$ 及频率 $a\ne0$。在一个**固定**的系数剩余嵌入处工作；其剩余特征记为 $\ell$。要求
$$\ell\nmid p(p^2-1).\tag{173.3}$$
实际 Tate 分母素数自动满足这一条件。

定义有限矩阵行
$$
\boxed{
\mathcal C_{\theta_u}(a,b)
=\frac1{pd}\sum_{x\in\mathbb F_p}\sum_{h\in H}
\psi(-ax)\theta_u(h)^{-1}
\operatorname{Tr}R_{\theta_u}(u_xh d_{a/b}),
\qquad b\ne0.}
\tag{173.4}
$$
令 $\mathcal O$ 为足够大的系数离散赋值环，且所有有限角色在其中分裂，置
$$
\mathfrak C_{u,a}
=\bigl(\mathcal C_{\theta_u}(a,b):b\in\mathbb F_p^\times\bigr),
\qquad
\mathfrak C^{\mathrm{prim}}_{p,d,a}
=\sum_{u\in(\mathbb Z/d\mathbb Z)^\times}\mathfrak C_{u,a}.
\tag{173.5}
$$

**定理 173.1。** 在上述条件下：

1. 同一个实际有限有理商 $B_\alpha$ 提供每个 $u$ 和每个 $\epsilon\in\{1,-1\}$ 的有限角色对
   $$\{\theta_u\vartheta^\epsilon,(\theta_u\vartheta^\epsilon)^{-1}\}$$
   对应的整微分。它们可以来自不同的共轭新形式 $f^\sigma$；不声称同一个指定 $f$ 的两个中心值都由 (173.2) 单独推出。
2. R169 的精确指定行理想满足
   $$
   \boxed{
   \mathfrak C_{u,a}
   =\mathfrak W_{\theta_u,\theta_u\vartheta,a}
   +\mathfrak W_{\theta_u,\theta_u\vartheta^{-1},a}.}
   \tag{173.6}
   $$
   这是整理想等式，不只是特征零子空间等式，也没有将两行可能相消忽略。
3. 若 $\mathfrak C^{\mathrm{prim}}_{p,d,a}=\mathcal O$，则这个实际有限商在该尖点给形式浸入。因而实际非尖点的分母素数必须满足
   $$
   \boxed{\mathfrak C^{\mathrm{prim}}_{p,d,a}
   \subset\mathfrak m_{\mathcal O}.}
   \tag{173.7}
   $$
4. 若同时有 R69 的实际有限三次 Steinberg 商，则旧三色行理想与 (173.5) 必须在**同一** $a$、同一实际尖点和同一剩余嵌入下共同消失。

R169 中跨不同新形式的同余可能补出额外整微分，所以 (173.7) 仍只是实际分母存在的必要条件，不是完整最优商不浸入的充分条件。

## 2. 固定加性角色的系数自同构

由于 $(pd,3)=1$，圆分域的交为
$$\mathbb Q(\mu_{pd})\cap\mathbb Q(\mu_3)=\mathbb Q.$$
因此存在一个系数自同构 $\sigma$，在 $\mu_{pd}$ 上恒等、在 $\mu_3$ 上取逆。它固定 $\psi$ 和 $\theta$ 的所有值，而
$$\sigma(\theta\vartheta)=\theta\vartheta^{-1}.\tag{173.8}$$
更一般地，中国剩余定理给每个 $u\in(\mathbb Z/d\mathbb Z)^\times$、$\epsilon=\pm1$ 一个系数自同构 $\sigma_{u,\epsilon}$，满足
$$
\sigma_{u,\epsilon}|_{\mu_p}=1,
\qquad \sigma_{u,\epsilon}(\theta)=\theta_u,
\qquad \sigma_{u,\epsilon}(\vartheta)=\vartheta^\epsilon.
\tag{173.9}
$$
这些自同构可延拓到包含新形式系数及所有有限角色值的正规系数域；再延拓到 $\overline{\mathbb Q}$。不要求它们固定 $f$ 的所有 Fourier 系数。

$f^\sigma$ 仍为权二、平凡 nebentype、水平 $p^2$ 的归一化新形式。其有限类型的特征标就是 $R_{\theta_u}$：R169 所列四种特征标值在作用 $\sigma$ 后逐项变为 $\theta_u$ 的同一公式。因此原始 $\theta$ 的所有共轭确为同一有理兼容系统轨道的实际类型，不能只把它们当形式上可选的其他模形式。

R169 的矩阵只依赖有限类型、实际 $\psi$、Cartan 嵌入及角色 $\varphi$，不依赖 $f$ 的其他 Fourier 系数。所以换成这些真实 $f^\sigma$，仍严格得到 (173.4) 和 (173.6) 中所写的同一指定行。

## 3. 有理商、实际下降与固定剩余嵌入

需要区别两个操作：本文从一个有理商中取其**已经包含的共轭微分**，然后全部在同一个剩余嵌入评价；没有将某条已经取模的等式连同其素理想一起作 Galois 变换。

### 3.1 完整有理轨道必含全部共轭

R166 的有理投影是按完整兼容系统轨道构造的。故其在特征零的像，对任意系数自同构都稳定。若其中含有
$$V_f\otimes\operatorname{Ind}_K^{\mathbb Q}
((\theta\vartheta)\circ\lambda),$$
就含有该因子在 (173.9) 下的共轭。由 R172 §7 的真实 Hecke/有限中心数域作用与 Kummer 论证，原轨道的实际有理投影像已经有有限有理点群；取同一有理投影像里的共轭不会引入新的秩零假设。每个 $B_\alpha$ 是这个投影像的实际 $\mathbb Q$ 子簇，故同样有限。

这一步不要求中心值在两个非等价轨道之间相等，也不要求另行证明每个共轭数值的非消失。使用的是已由一个非零中心值和 R172 的中央域 Kummer 拼接证明的**实际有理商**有限性。

可能的 Schur 指数影响实际有理投影像中绝对因子的重数，不会使有理投影失去系数共轭稳定性，也不妨碍 R172 在中央域一个嵌入处应用 Kummer 注入。相同地，扩大系数域只把已有因子分裂；不会增加假想的阿贝尔簇商。这里不要求整个投影像属于一个单独的 $\mathbb Q$ 简单同源类型。

### 3.2 扭曲下降只增加逆字符取向

若将 $\sigma$ 同时看作算术 Galois 元素，实际扭曲的下降还会作用一个 $r(\sigma)\in N$。由于 (173.9) 固定 $\mu_p$，其行列式为一；所以它保持正在使用的几何 Weil 配对分支。R169 §5 已将 $g^{-t}$ 的对偶下降同时共轭到实际 $N$ 作用。

在 Cartan 上，$N$ 的共轭仅有两个可能：恒等或取逆。因此一个角色对
$$\{\varphi,\varphi^{-1}\}$$
在算术共轭后恰为
$$\{\varphi^\sigma,(\varphi^\sigma)^{-1}\}.$$
由 (173.9)，这正是定理中的
$$\{\theta_u\vartheta^\epsilon,
(\theta_u\vartheta^\epsilon)^{-1}\}.$$
没有产生另一个不受控的 Cartan 嵌入。若用同一基变换表达下降，Cartan、幺幂群和尖点同时变换，随后回到已经固定的实际坐标即可；两条逆字符都在同一个保留的有限子空间中。

### 3.3 同一素理想处的整性

固定一次嵌入 $\iota_\ell:\overline{\mathbb Q}\hookrightarrow\overline{\mathbb Q}_\ell$ 和一个包含全部需要系数的离散赋值环 $\mathcal O$。对于每个 $\sigma$，先取有理商中相应的 $f^\sigma$ 微分，再用**同一个** $\iota_\ell$ 评价。

所有 $f^\sigma$ 的 Fourier 系数都是代数整数，归一化首系数都是一。R169 的真实拉回、单有限类型交格及最优商余切交格论证逐个适用。因此各有限角色投影确为这个实际有理商的整微分。

不必有 $\iota_\ell\circ\sigma=\iota_\ell$，也不假定 $\sigma$ 保持某个素理想。反过来，恰因我们不是将取模式作 Galois 变换，所以不存在把指定 $\ell$ 上方素理想换走的问题。固定 $\mu_p$ 保证所有矩阵中的加性根 $\psi$ 相同；固定 Cartan 模型保证所有 $a$ 相同。

这证明定理 173.1(1)，也澄清为何 R172 中“若要使用两个不同轨道须各有非零中心值”的保守说法并不阻碍这里：本文识别的是**同一轨道内**已经出现的有限类型和角色方向，允许对应的新形式改变。

## 4. 三次子群投影：精确秩二及整理想等式

固定 $u$。用 $L$ 表示 R169 中 $R_{\theta_u}$ 的饱和交格，以 $v_b$ 为其整 Kirillov 基。有限群矩阵在 $\mathcal O$ 上整，且 $p$、$p+1$、$d$ 都是单位。

记
$$
e_\varphi=\frac1{p+1}\sum_{c\in\overline C}
\varphi(c)^{-1}R_{\theta_u}(c),
\qquad
e_{H,\theta_u}=\frac1d\sum_{h\in H}
\theta_u(h)^{-1}R_{\theta_u}(h).
\tag{173.10}
$$
因为 $\overline C/H$ 阶为三，$\theta_u|_H$ 的三个延拓恰为
$$\theta_u,\quad\theta_u\vartheta,\quad\theta_u\vartheta^{-1}.$$
因此在整个群代数中有
$$e_{H,\theta_u}=e_{\theta_u}+e_{\theta_u\vartheta}
+e_{\theta_u\vartheta^{-1}}.$$
而尖点型的准确 Cartan 限制为
$$R_{\theta_u}|_{\overline C}
=\operatorname{Reg}_{\overline C}-\theta_u-\theta_u^{-1}.$$
这里 $\theta_u|_H$ 阶为 $d>4$，故 $\theta_u^{-1}$ 的限制不是 $\theta_u|_H$。于是 $e_{\theta_u}=0$，另两项各秩一，得到
$$
\boxed{e_{H,\theta_u}
=e_{\theta_u\vartheta}+e_{\theta_u\vartheta^{-1}},
\qquad\operatorname{rank}e_{H,\theta_u}=2.}
\tag{173.11}
$$
这些都是整幂等元，并且
$$e_\varphi=e_{H,\theta_u}e_\varphi=e_\varphi e_{H,\theta_u}
\quad(\varphi=\theta_u\vartheta^{\pm1}).\tag{173.12}$$

令 $\Lambda$ 为同一个指定尖点的首系数泛函。一个整矩阵 $E$ 的指定行理想可写为 $\Lambda(EL)$。由 (173.11)，
$$\Lambda(e_{H,\theta_u}L)
\subset\Lambda(e_{\theta_u\vartheta}L)
+\Lambda(e_{\theta_u\vartheta^{-1}}L).$$
由 (173.12) 和 $e_\varphi L\subset L$，反向的每一项也包含在 $\Lambda(e_{H,\theta_u}L)$ 中。故两边相等，证明 (173.6)。

特别地，即使两个单独行逐列之和出现相消，乘回两个**整**投影仍恢复各行，因而不能使整个合并行理想变小。这是需要保留全行而不能只看对角迹的原因。

## 5. 显式指定行与旧三色行

R169 给
$$\Lambda(e v_b)=\operatorname{Tr}\bigl(P_a eR_{\theta_u}(d_{a/b})\bigr),
\qquad P_a=\frac1p\sum_x\psi(-ax)R_{\theta_u}(u_x).$$
代入 $e=e_{H,\theta_u}$，即为 (173.4)。其全部特征标值为
$$
\operatorname{Tr}R_{\theta_u}(g)=
\begin{cases}
p-1,&g=1,\\
-1,&g\text{ 为非平凡幺幂元},\\
0,&g\text{ 为分裂正则半单元},\\
-\theta_u(\gamma)-\theta_u(\gamma^p),&g\text{ 为非分裂正则半单元}.
\end{cases}
\tag{173.13}
$$
所有输入均为同一实际有限群模型中的精确代数数。

设 $\mathfrak J_{p,a}^{\mathrm{St}}$ 是 R72 中同一个实际尖点的三色 Steinberg 行理想；等价地，在 $\ell\nmid3p$ 时可使用旧 $S(a),S(-a)$ 的共同零条件。如果相应实际三次 Steinberg 中心值非零，则由 R69/R72 它来自实际有限商。与本定理的实际有限商取积并最优化，得到可用的必要理想
$$
\mathfrak J_{p,a}^{\mathrm{St}}
+\mathfrak C^{\mathrm{prim}}_{p,d,a}
\subset\mathfrak m_{\mathcal O}.
\tag{173.14}
$$
旧商和新商的非零中心值前提分别保留。两者相加只是组合已经证明有限的实际商，不将一个商的非消失转移给另一个。

由定理 173.1(1) 和 R169 的最优商整交格，(173.5) 中任一单位首系数都给形式浸入。R72 的实际 Tate 剩余圆盘、全尖点除子和有限有理点群论证随后排除实际分母。这证明 (173.7) 和 (173.14) 的必要性。

## 6. 新增内容与仍需证明的精确问题

本结果将“单个 $f$ 上四条角色线是否都有非零中心值”的表述收紧：**一个实际非零中心值即可在同一个有限有理商中同时取得所有原始有限类型共轭和两个三次方向。** 它们无需来自同一个 $f$。这一点使用完整有理轨道，而不是用圆分 Galois 对称移动指定素理想。

相应的有限问题可以准确改写为：在实际 $\ell\equiv\pm1\pmod p$、同一个指定 $a$ 与剩余嵌入下，是否可能同时有
$$
S(a)=S(-a)=0,
\qquad
P_a e_{H,\theta_u}=0
\quad\text{对所有 }u\in(\mathbb Z/d\mathbb Z)^\times?
\tag{173.15}
$$
这里矩阵等式是整行的模 $\ell$ 消失；不能替换为较弱的 $\operatorname{Tr}(P_a e_{H,\theta_u})=0$。

(173.11) 给秩二、迹二；(173.3) 给 Maschke 半单性。这两点仍不能单独排除 (173.15)：一个非零幂等元可能在预定行上全为零，迹二只约束所有行之和。同样，(173.9) 允许增加实际商里已经存在的共轭微分，不允许改变频率 $a$。本文没有将这两类全称/存在量词混同。

(173.14) 是否为单位，及变化 $E,K,p$ 时是否总有一个满足 (173.2) 的实际因子，仍是真正的主问题。本文没有证明全称非消失，也没有消除 Serre uniformity 的剩余分支。

## 7. 输入定位

- [R166](R166-small-inertia-cuspidal-positive-sign-quotients.md) §§2、5：真实尖点类型非空、Cartan 字符缺失公式、完整有理兼容系统轨道及每个实际配对分支上的商。
- [R169](R169-cuspidal-whittaker-lattices-and-the-specified-cusp-row.md) §§2–6：真实模映射首系数一、饱和单类型整格、有限群整投影、实际下降取向及精确指定行；§7：形式浸入的充分方向与分母的必要方向。
- [R172](R172-cuspidal-central-values-and-actual-rank-zero-quotients.md) §§3–7：Kings–Loeffler–Zerbes 已发表的一般新形式秩零接口，以及实际有理投影像的中央数域作用和 Kummer 拼接；另有一个绝对 Tate 因子消失即给实际 $\mathbb Q$ 简单商有限的除环引理。
- [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)、[R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：实际三次 Steinberg 商及同一个 Tate 尖点/原始根的旧三色行。

本篇新增的系数域自同构、正规化子取向与整理想等式全部自含；没有使用新的未发表定理或有限素数扫描。
