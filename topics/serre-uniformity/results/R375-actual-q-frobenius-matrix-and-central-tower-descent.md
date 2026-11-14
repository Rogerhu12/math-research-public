# R375：实际 q-Frobenius 矩阵与全裂塔的中央下降

**状态：已证明；有限局部环运算已完成。** 固定 R171 的同一个
\(p=43\)、776 bit 素数 \(q\)、\(F/K\)、正算术 Artin 元 \(\sigma\)、
原始生成元 \(y\) 和主化元
\[
 K=\mathbf Q(i),\quad F=K(z),\quad
 \Delta=\langle\sigma\rangle\simeq C_{44},\quad
 \alpha=1+89460y,\quad\omega=8+25i.
 \tag{375.1}
\]
本文没有把 \(y\) 与普通单位生成元 \(z\) 混同；二者按 R327 的准确
全局等式 \(z=h(y)/2\) 连接。

令 \(F^{(43)}\) 为 \(F\) 的最大仅在 43 上方分歧的 pro-43 扩张，
\(G_{F,43}=\operatorname{Gal}(F^{(43)}/F)\)。R327 已证明该群自由秩 45。
令 \(\mathfrak q_j=\sigma^j\mathfrak q_0\) 为 \(q\) 在 \(F\) 中的全部
44 个素点，\(\varphi_j\) 为它们在
\[
 \mathcal A=G_{F,43}^{\rm ab}/43\simeq\mathbf F_{43}^{45}
\]
中的**正算术 Frobenius**。本条的实际算术结论为
\[
 \boxed{\dim_{\mathbf F_{43}}
         \langle\varphi_0,\ldots,\varphi_{43}\rangle=41.}   \tag{375.2}
\]
其全部线性关系恰为下文三个明确向量，角色为 \(\chi^{16},\chi^{-16},
\chi^{22}\)，其中 \(\chi(\sigma)=\omega\)。

进一步，令 \(\mathcal M\subset F^{(43)}\) 为使全部 \(\mathfrak q_j\)
全裂的最大 pro-43 扩张，\(\mathcal G=\operatorname{Gal}(\mathcal M/F)\)。则

\[
 \boxed{d(\mathcal G)=4,\qquad r(\mathcal G)\le3.}           \tag{375.3}
\]
这里 \(d\) 为最小生成元数，\(r\) 为最小关系数。本文不声称这三个关系为空。

更强的完整塔结论是：置
\[
 F_0=F^{\langle\sigma^{22}\rangle}=K(z+z^{-1}),
 \qquad [F:F_0]=2.
\]
若 \(\mathcal M_0/F_0\) 是最大仅在 43 分歧、且 \(q\) 的全部上方素点
全裂的 pro-43 扩张，则
\[
 \boxed{\mathcal M=F\mathcal M_0,\qquad
 \operatorname{Gal}(\mathcal M/F)
 \simeq\operatorname{Gal}(\mathcal M_0/F_0).}                \tag{375.4}
\]
这个下降是整个非阿贝尔塔的结论，不只是一阶角色的比较。

实际 Norm 原像与 \(\mathcal L\) 仍未求值。\(\mathcal M\) 是仅在 43
分歧、在 \(q\) 全裂的塔，和 R311 的 \(L=FL_q\) 是不同的扩张；
后者在 \(q\) 分歧。本文没有把 (375.3)–(375.4) 代入一个尚未证明的
Norm 或高阶互反公式。

## 1. 一个完全有限的局部 Kummer 商

### 1.1 准确的有限环

沿用 R185/R327 的规范
\[
 \pi^{44}=C43,\quad C=70375455224064\equiv38\pmod {43},
 \qquad \sigma\pi=[\omega]^{-1}\pi,
 \qquad F_{43}=\mathbf Q_{43^2}(\pi).
 \tag{375.5}
\]
在
\[
                     R=\mathcal O_{F_{43}}/(\pi^{46})      \tag{375.6}
\]
中，每个元素唯一表示为 \(\sum_{j=0}^{43}a_j\pi^j\)：\(a_0,a_1\)
属于 \((\mathbf Z/43^2)[i]\)，其余 \(a_j\) 属于 \(\mathbf F_{43^2}\)。
相乘时只需保留次数不超过 45 的项，并用
\(\pi^{44}=C43\)、\(\pi^{45}=C43\pi\) 归约。
次数至少 46 的项为零，且 \(43\pi^j=0\) 对 \(j\ge2\) 成立。
这说明程序的不同系数精度是该有限环的准确表示。

程序直接在此环中求解
\[
 u^{44}-1+\sum_{j=1}^{43}\frac{c_j}{C}\pi^j u^j=0,
 \qquad u\equiv1\pmod\pi,
 \qquad y=\pi u.
 \tag{375.7}
\]
其导数为单位，故有限 Hensel 唯一性选择的正是同一个规范 \(y\)。
六次 Newton 迭代后方程严格为零，且原 \(P_y(y)=0\) 也逐系数检查。
再以 R327 的同一个 \(h\) 得到 \(z=h(y)/2\)。

Teichmüller 元实际为
\[
 [\omega]\equiv352+197i\pmod {43^2};                        \tag{375.8}
\]
程序检查其阶为 44。对每个普通元素，所有 \(\sigma^j\) 的值均按
(375.5) 直接计算，所以此次没有更换 Artin 标签。

### 1.2 深度 46 已包含全部 43 次幂信息

令 \(U^r=1+\pi^r\mathcal O_{F_{43}}\)。因
\(2>44/(43-1)\)，局部指数和对数在 \(U^2\) 及其加法格之间互逆，故
\[
                        (U^2)^{43}=U^{46}.                \tag{375.9}
\]
若 \(v\in U^1\setminus U^2\)，写 \(v=1+a\pi+O(\pi^2)\)，其中
\(\bar a\ne0\)。二项式公式给
\[
              v^{43}=1+\bar a^{43}\pi^{43}
                         +O(\pi^{44}).                    \tag{375.10}
\]
所以 \((U^1)^{43}/U^{46}\) 的维数为 2，且非平凡元素的首个非零层为 43。

准确的两项生成元在 \(R\) 中为
\[
 \begin{aligned}
 G_1=(1+\pi)^{43}&=1+\pi^{43}+43\pi,\\
 G_i=(1+i\pi)^{43}&=1-i\pi^{43}+43i\pi.
 \end{aligned}                                             \tag{375.11}
\]
所有中间二项式系数均含因子 43；除了线性项，其总赋值至少 46，
故以上就是完整有限等式。

设
\[
 \mathcal J=(1,2,\ldots,42,44,45),\qquad
 b_{r,0}=1+\pi^r,\quad b_{r,1}=1+i\pi^r\quad(r\in\mathcal J).
 \tag{375.12}
\]
这 88 个元素在 \(U^1/(U^1)^{43}\) 中组成一组 \(\mathbf F_{43}\) 基。
证明如下：若其系数在 \(0,\ldots,42\) 的乘积非平凡，取首个系数非零的
深度 \(r\)。首项是一个非零 \(\mathbf F_{43^2}\) 元素乘 \(\pi^r\)。
当 \(r\le42\) 时，由 (375.10) 不可能是 43 次幂；当 \(r=44,45\) 时，
任何首项没有出现在 43 层的 43 次幂已落入 \(U^{46}\)，仍不可能。
所以它们独立。另一方面
\[
 \#U^1/U^{46}=43^{90},\qquad
 \#(U^1)^{43}/U^{46}=43^2,
\]
商的维数恰为 88，证毕。

程序先除去剩余单位的唯一 Teichmüller 提升，再依次用 (375.12)
消去 1 至 42 层，用 (375.11) 消去 43 层，最后消去 44、45 层。
每次所得 88 个坐标均属于 \(\mathbf F_{43}\)，且最后余项严格为 1。
(375.9) 保证坐标为零当且仅当原元素是实际局部域中的 43 次幂。
所有 88 个基向量以及两个 43 次幂生成元都已逐一验证。

## 2. 普通单位与实际 q-Frobenius 的矩阵

### 2.1 普通单位列

按 R327 的固定顺序，取 43 个普通单位
\[
 \eta=(\varepsilon_0,\ldots,\varepsilon_{21},
       \sigma\varepsilon_0,\ldots,\sigma\varepsilon_7,
       \sigma\varepsilon_9,\ldots,\sigma\varepsilon_{21}).
 \tag{375.13}
\]
R327 已证明它们组成 \(E_F/E_F^{43}\) 的基，且其局部像饱和。
本次在 (375.12) 的完整基中重新计算其 \(88\times43\) 矩阵 \(U\)，
再次得到 \(\operatorname{rank}U=43\)。

由 R264 的 \(\operatorname{Cl}(F)[43]=0\) 和 R327 的类域序列，
\[
 \mathcal A\simeq
 U^1/(\overline{E_F}(U^1)^{43}).                            \tag{375.14}
\]
所以这个单位矩阵给出的是所需全局阿贝尔化的准确 45 维商。

### 2.2 Frobenius 的正算术符号

R171 已证明 \(N_{F/K}\alpha=-q\)，且 \(\alpha\) 是 \(\mathfrak q_0\)
的整主化元。因 \(F/K\) 为 Galois 扩张，这也给出 \(q\) 完全分裂的
44 个素点
\[
 (\alpha_j)=\mathfrak q_j,
 \qquad\alpha_j=\sigma^j\alpha,
 \qquad0\le j<44.
 \tag{375.15}
\]
在仅在 43 分歧的扩张中，\(\alpha_j\) 的局部单位部分在所有
\(\ell\ne43,q\) 处的 Artin 值均为零；在 \(\mathfrak q_j\) 处，赋值一
给正算术 Frobenius。主 idèle 的互反乘积为一，因此
\[
                    \boxed{\varphi_j=-[\alpha_j]_{43}
                           \pmod{\overline E_F}.}          \tag{375.16}
\]
这个负号保存在证书中。以下核关系不受整体负号影响，但没有因此省略其
算术规范。

### 2.3 全部关系与秩 41

将 (375.16) 的 44 列加入 \(U\)，得到 \(88\times87\) 矩阵
\(A=(U\mid-\alpha_0,\ldots,-\alpha_{43})\)。本次实际得到
\[
 \operatorname{rank}A=84,
 \qquad
 \boxed{\det A_{\mathrm{specified}\ 84\times84}=5\pmod{43}.}
 \tag{375.17}
\]
该子式使用全部 43 个普通单位列及 Frobenius 列 \(j=0,\ldots,40\)；
全部有序行号记录在证书中。因此这 41 个 Frobenius 已线性独立。

定义三个长度 44 的向量
\[
 v^+_j=\operatorname{Re}(\omega^{16j}),\qquad
 v^-_j=\operatorname{Im}(\omega^{16j}),\qquad
 v^{\rm quad}_j=(-1)^j\qquad(0\le j<44).
 \tag{375.18}
\]
程序分别求得并保存 43 个普通单位修正指数 \(a_t(v)\in\mathbf F_{43}\)，
并在有限环中实际核验完整乘积
\[
 \boxed{\frac{\prod_{j=0}^{43}\alpha_j^{v_j}}
                {\prod_{t=0}^{42}\eta_t^{a_t(v)}}
          \in F_{43}^{\times43}.}                          \tag{375.19}
\]
这里所有指数取 \(0,\ldots,42\) 中的整数代表。
核验不仅是把存储矩阵相乘：程序重新相乘这些实际局部元素、除去普通单位
修正，再按 §1.2 消元，88 个坐标全部为零。

例如，\(v^+\) 和 \(v^-\) 的各 11 项周期分别为

~~~text
v+ : 1,26,18,7,2,11,11,2,7,18,26
v- : 0,23,35,34,13,40,3,30,9,8,20
~~~

这三个关系的全部 43 项单位修正指数、完整局部余项以及完整矩阵均已
保存在证书中。(375.16)、(375.19) 给
\[
 \sum_jv^+_j\varphi_j=\sum_jv^-_j\varphi_j
      =\sum_j(-1)^j\varphi_j=0.                            \tag{375.20}
\]
\(\omega^{16}\) 的阶为 11，且不在 \(\mathbf F_{43}\) 中，故前两向量
独立；第三个周期二向量不在它们的周期 11 空间中。
因此它们给出三个独立关系，与 (375.17) 合起来证明 (375.2)，并证明没有
遗漏其他线性关系。

\(\sigma\) 按 \(j\mapsto j+1\) 作用于素点置换模。
(375.18) 的前两向量生成复化后特征为 \(\chi^{16},\chi^{-16}\) 的二维
分量；第三个生成 \(\chi^{22}\)。因此角色描述也保留了同一 \(\sigma\)
方向。

由 (375.2)，使全部 \(\mathfrak q_j\) 全裂的最大仅在 43 分歧的
**初等阿贝尔** 43 扩张，次数准确为
\[
                      43^{45-41}=43^4=3418801.              \tag{375.21}
\]
证书还保存了 \(A\) 的四个独立左零向量；它们给出这四个全局类域角色的
完整局部坐标。这里已准确指定相应类域，但未生成其定义多项式。

## 3. 四生成元、至多三关系的非阿贝尔群

在自由 pro-43 群 \(G_{F,43}\) 中，为每个 \(\mathfrak q_j\) 选择一个
正 Frobenius 元 \(g_j\)。其共轭选择不影响以下闭正规包。由于这些素点
在 \(F^{(43)}/F\) 中未分歧，使其全裂恰好是杀掉相应 Frobenius，故
\[
 \mathcal G
  =G_{F,43}/\overline{\langle\!\langle
                  g_0,\ldots,g_{43}\rangle\!\rangle}.
 \tag{375.22}
\]
由 (375.14)–(375.17)，\(g_0,\ldots,g_{40}\) 的 Frattini 像独立。
自由 pro-p 群的基定理允许把它们扩为 \(G_{F,43}\) 的一组 45 元自由基。
杀掉这 41 个基元之后留下秩四的自由 pro-43 群；剩下的
\(g_{41},g_{42},g_{43}\) 给出至多三个关系。

44 个原关系的 Frattini 秩已经准确为 41，所以这三个剩余关系在新的
四生成自由群中都属于 Frattini 子群；它们不再减少生成元数。
这证明 (375.3)。其三个实际非线性字尚未求出；本文既没有声称关系数
恰等于三，也没有声称 \(\mathcal G\) 自由。

## 4. 中央二次元在整个塔上消失

### 4.1 一阶恒等已作全部有限核验

在局部环中，\(\sigma^{22}\pi=-\pi\)、\(\sigma^{22}i=i\)。
程序对 (375.12) 的全部 88 个基向量逐一计算
\[
 [\sigma^{22}b_{r,c}]-[b_{r,c}]
 \in U^1/(U^1)^{43},
\]
并在 (375.17) 的四个左零向量上求值，得到完整 \(88\times4\) 零矩阵。
这四个向量因 \(\operatorname{rank}A=84\) 而恰好检测商空间，故准确证明
\[
          \sigma^{22}\text{ 在 }\mathcal G/\Phi(\mathcal G)
          \text{ 上作用为恒等}.                            \tag{375.23}
\]
该作用是类域论的自然等变作用。普通单位空间与全部 \(q\)-Frobenius
空间都在 \(\sigma^{22}\) 下稳定，因此所取商上的作用确有定义。

### 4.2 有限阶提升与 Frattini 核引理

需要使用下列群论事实，并保留其有限阶条件。

**引理。** 设 \(P\) 为有限生成 pro-p 群，\(p\) 为奇素数。
一个阶整除二的连续自同构若在 \(P/\Phi(P)\) 上为恒等，则它在 \(P\)
上为恒等。

**证明。** 先设 \(Q\) 为有限 p 群，取 \(Q/\Phi(Q)\) 的一组有序基。
所有提升该基的有序元组均生成 \(Q\)：否则它们生成的真子群包含于
某个极大子群，和基的满射性矛盾。这些提升元组的数目为
\(|\Phi(Q)|^{d(Q)}\)。
\(\ker(\operatorname{Aut}(Q)\to\operatorname{Aut}(Q/\Phi(Q)))\)
保持这个集合并自由作用，因为固定一个生成元组的自同构只能是恒等。
所以该核的阶整除一个 p 次幂，本身为 p 群。

对有限生成 pro-p 群取所有有限特征商。它们构成一个余终族：同一给定
指数的开子群只有有限个，取其交即可得到所需特征开子群。
所给自同构在每个有限商的 Frattini 商上仍为恒等，所以其像同时有
p 次幂阶与整除二的阶，只能为恒等。所有有限特征商分离点，故原自同构
也是恒等。同样的逆极限说明，有限生成 pro-p 群的整个 Frattini 核
自同构群是 pro-p 群。证毕。

现在全部 \(\mathfrak q_j\) 的集合在 \(\Delta\) 下稳定，且分歧条件也
稳定，因此最大性使 \(\mathcal M/K\) 为 Galois 扩张。考察
\(\sigma^{22}\) 的原像，得到
\[
 1\longrightarrow\mathcal G
 \longrightarrow\operatorname{Gal}(\mathcal M/F_0)
 \longrightarrow C_2\longrightarrow1.                    \tag{375.24}
\]
这里确有一个**阶恰为二**的提升 \(\widetilde\delta\)：在每个由
\(\mathcal G\) 的特征开子群给出的有限商中，Sylow 二子群的阶为二。
沿商映射，给定这样的二阶元总可在其奇数阶核的原像中用 Sylow 定理
再次提升；有限集合的逆极限紧性遂给一个二阶元。
这一步没有任取一个可能无限阶的 Frobenius 提升。

(375.23) 说明其共轭作用在 \(\mathcal G/\Phi(\mathcal G)\) 上恒等。
提升的改变只给内自同构，不改变这一 Frattini 作用。
引理迫使 \(\widetilde\delta\) 与整个 \(\mathcal G\) 交换，因而
\[
 \operatorname{Gal}(\mathcal M/F_0)
            =\mathcal G\times\langle\widetilde\delta\rangle.
 \tag{375.25}
\]

## 5. 最大塔准确下降到 F0

令 \(M_0=\mathcal M^{\langle\widetilde\delta\rangle}\)。由 (375.25)，
\(M_0/F_0\) 是 pro-43 Galois 扩张，且
\[
 M_0F=\mathcal M,
 \qquad M_0\cap F=F_0,
 \qquad\operatorname{Gal}(M_0/F_0)\simeq\mathcal G.           \tag{375.26}
\]
下面核实 \(M_0\) 具有宣称的分歧和全裂条件及最大性。

**有限素点的分歧。** 对 \(M_0/F_0\) 的任意有限 Galois 子扩张 \(N/F_0\)，
\(NF/F\subset\mathcal M/F\) 在 43 之外未分歧。
因此在任意 \(v\nmid43\) 处，\(NF/F_0\) 的分歧指数整除
\([F:F_0]=2\)。另一方面，\(N/F_0\) 的分歧指数为 43 次幂；
它整除前者，所以只能为一。故 \(M_0/F_0\) 仅在 43 处分歧。

**q 处的全裂。** R171 的 \(q\) 在 \(F/K\) 中完全分裂，所以在
\(F_0/K\) 中也完全分裂，且 \(F/F_0\) 在每个 \(q\) 素点处都是分裂
二次扩张。具体地，\(\sigma^{22}\) 把
\(\mathfrak q_j\) 与 \(\mathfrak q_{j+22}\) 配成 22 对；其下方就是
\(F_0\) 的全部 22 个 \(q\) 素点。
对任何上述 \(N\)，由于 \(NF/F\) 在全部 \(\mathfrak q_j\) 全裂，
而 \(F\) 与 \(F_0\) 在这些相应完备化上相同，\(N/F_0\) 也在全部
\(q\) 素点全裂。

**最大性。** 反过来，设 \(N/F_0\) 是仅在 43 分歧且在全部 \(q\)
素点全裂的任意 pro-43 Galois 扩张。其与二次扩张 \(F/F_0\) 线性不交，
且 \(NF/F\) 具有同样条件，所以 \(NF\subset\mathcal M\)。
\(\widetilde\delta\) 在 \(N\) 上的限制属于 pro-43 群
\(\operatorname{Gal}(N/F_0)\)，但其阶整除二，因此必须平凡。
故 \(N\subset M_0\)。这证明 \(M_0=\mathcal M_0\)，即 (375.4)。

最后，R219 的 \(\sigma^{22}z=z^{-1}\) 给
\(F_0=K(z+z^{-1})\)：\(z\) 在该域上满足二次方程，且不被
\(\sigma^{22}\) 固定，次数正好为二。

## 6. 已执行验证与尚未计算的数据

交付文件为

- `scripts/verify_r375_q_frobenius_matrix.py`；
- `notes/r375_q_frobenius_matrix_certificate.json`；
- 本证明。

运行命令为

~~~sh
python scripts/verify_r375_q_frobenius_matrix.py notes \
  --certificate notes/r375_q_frobenius_matrix_certificate.json --progress
~~~

程序仅用 Python 标准库，直接在准确有限环中重算：规范 \(y,z\)、
全部 88 个局部基向量、浅层 43 次幂核、43 个普通单位、44 个实际主化元
共轭、秩 84 子式、三条实际局部乘积关系、四个商角色，以及完整的
\(\sigma^{22}\) 商作用零矩阵。输入 SHA256 和全部矩阵数据均保存在
证书中。R171 的全局主化和 R327 的全局单位及自由性作为已证明输入。

作为独立开发复核，同一 Frobenius 秩还曾由完整 Artin–Hasse 对数坐标
得到一致的 41；最终核验器不依赖这项对数计算或其尾界。

本文得到的是准确的阿贝尔 Frobenius 数据和由有限阶作用强迫的整个塔
下降。\(g_{41},g_{42},g_{43}\) 在四生成自由群中的三个实际关系字没有
计算；R311 的固定 \(X,Y\)、其 \(q\) 相位和规范 \(\mathcal L\) 同样没有
计算。证书明确保留

~~~text
actual_norm_preimage_computed: false
actual_L_computed: false
nonabelian_q_Frobenius_computed: false
~~~

特别地，(375.19) 是主化元乘积经普通单位修正后的**局部** 43 次幂，
没有把这些非单位全局乘积冒称为 \(L/F\) 的真实 Norm 原像。
R200 的外支撑 Artin 修正规则仍然适用。

主要依赖为仓库内 R171、R185、R219、R243、R264、R327。
仅在 p 分歧的类域序列及 p-rational 自由性判据的原刊定位已在 R327
给出；本条没有新增未经核读的外部数论定理。
