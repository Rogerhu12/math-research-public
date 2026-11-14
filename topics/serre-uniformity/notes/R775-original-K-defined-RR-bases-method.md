# R775：原商曲线的实际 K 定义 Riemann–Roch 基

日期：2026-11-14。状态：**方法已证明，公开运行前工程；未预称实际秩或子式已返回。**

本次接续已完成的 R771。原 \(146/694/1514\) 维空间已有具体配方，但这些配方的算术定义域仍含 \(\xi_{82}\)。R772 给出的半线性行列式迹将把它们变成原 \(K\) 上定义的基。这一步直接服务于原 \(y\in L(Y)\) 的准确线性恢复；不会把尖点 Fourier 系数也误认为在 \(K\)。

## 1. 已完成输入和复用边界

唯一大输入来自公开仓库实际 R771：

- run 43628998192，source 49abc04d7867c9f56911866494692c597cf642d7；
- artifact 14127715743，名称 serre-global-R771-p41-original-quotient-RR-bases-43628998192-1；
- ZIP SHA256 e158bff06405576ce235745db26b6a2e35145d2b1f2d6978127b42a79e1e7c1c；
- manifest SHA256 024ed12029720cc1c5d7ec0612aa484b04cdde8f763fceb852a0fdeabc2c3d74；
- certificate SHA256 9eb870af949167895daa4e180c16848860f8fea1c9efe1b105ab3cd3a667009f；
- 原核心 SHA256 9cda269687a01c95c9c20695be771706bbddd37b1b8fedc8b9258386c3965d46。

输入的 85 个已完成阶段是 82 个 E1 行块、原 H82/标签文件、原 E4/E6/eta12 文件和原 M2 基文件。逐文件 SHA 与大小均与真实 manifest 核对，旧 configuration 不改写。全部 \(q_Y^{0},\ldots,q_Y^{1640}\) 的 E1 系数直接读取；原 determinant-one M2 行也直接读取。

源代码导入 R771 的通用原行选取、正常乘积与椭圆主部补全方法，但不调用其旧初始化、E1 生成、群生成或 level-one 展开。旧源文件自身 SHA 也被绑定。新产品全部使用新 configuration 和 R775 文件名；不能用改 tag 的办法冒充旧输入或新完成状态。

R735/R738/R745/R754/R759 的原模型、拓扑、有限向量、周期、整格和 degree 均不重算。原所选微分仍为 R759 第4号、degree1206，R764 的零平移仍保留。

## 2. 原 GL2 群和行列式代表

保留 R767 的
\[
H_{82}\subset\operatorname{SL}_2(\mathbf Z/82\mathbf Z),
\qquad |H_{82}|=252,
\]
其 mod2 分量为原 \(C_3\)，mod41 分量为原非分裂正规化子的 determinant-one 部分。定义
\[
G_{82}=C_3\times N_{\operatorname{GL}_2(\mathbf F_{41})},
\qquad |G_{82}|=10080,\qquad G_{82}/H_{82}\simeq\mathbf F_{41}^{\times}.
\]

对每个 \(d\in\mathbf F_{41}^{\times}\)，在原环面中选一个矩阵
\[
g_{d,41}=
\begin{pmatrix}a&-b\\ b&a+b\end{pmatrix},
\qquad a^2+ab+b^2=d.
\tag{775.1}
\]
用 CRT 将其 mod2 分量固定为恒等矩阵，得到 \(g_d\in G_{82}\)。\(d=1\) 明确取恒等矩阵，以直接复用原 M2 行。实际计算核对四十个代表的行列式、逆矩阵及对原全部 \(H_{82}\) 的共轭正规性。

必须使用行列式的模82奇数提升
\[
d_{82}=
\begin{cases}d,&d\text{ 为奇数},\\d+41,&d\text{ 为偶数}.
\end{cases}
\tag{775.2}
\]
它是 \(\det g_d\in(\mathbf Z/82\mathbf Z)^\times\)。在 \(\xi_{82}^{j\det g_d}\) 中直接填裸整数 \(d\) 会改变半线性 Galois 作用；源码保留 (775.2)。

## 3. 每个实际旧种子的半线性迹

R771 实际小证书给 146 个原种子
\[
B_r=\frac12\sum_{h\in H_{82}}E_{\lambda_r h}E_{\mu_r h}.
\]
它们的特征零配方和模739原行的非零 minor550已实际完成。

按照 R772 的原 GL2 半线性右作用，
\[
B_r*g_d
=\frac12\sum_{h\in H_{82}}
 E_{\lambda_r h g_d}E_{\mu_r h g_d}.
\tag{775.3}
\]
两个标签必须一起运输。本次每个种子的四十个移像按实际 \(H_{82}/\{\pm I\}\) 的126项计算；determinant-one一项完全读取旧 M2 行。

对 \(0\le j<40\) 定义
\[
\boxed{
T_{j,r}=\sum_{d\in\mathbf F_{41}^{\times}}
 \xi_{82}^{j d_{82}}\,(B_r*g_d).
}
\tag{775.4}
\]
这是 \(\operatorname{Tr}_{G_{82}/H_{82}}(\xi_{82}^jB_r)\)，因作用同时将标量 \(\xi_{82}\) 送到 \(\xi_{82}^{d_{82}}\)，所以不能改为普通无权平均。

每个 \(T_{j,r}\) 都由原半线性作用固定。R772 已把标准 G 模型与原 \(Y_K\) 通过
\[
E_6/\eta_{\rm Ded}^{12}=24\sqrt{-3}(2t-1)
\]
准确识别。因此 (775.4) 是原 \(K\) 上定义的权二形式。其参考尖点系数仍在原 \(M=L(\xi_{41})\) 中，未声称在 \(K\)。

## 4. 完备性与同一 prime739 的可靠秩选择

特征零中，\(1,\xi_{82},\ldots,\xi_{82}^{39}\) 是系数扩域的一个基，R772 的 Galois 下降说明所有 \(146\cdot40=5840\) 个 (775.4) 张成所需 \(K\) 空间。

此处还可直接证明在原 good prime739 上候选不会因单次约化丢掉整个秩。四十个
\[
x_d=\overline{\xi}_{82}^{\,d_{82}}
\]
两两不同，因原 \(\overline{\xi}_{82}=512\) 的阶恰为82，而这些 \(d_{82}\) 遍历模82单位。矩阵
\[
(x_d^j)_{0\le j<40,\ d\in\mathbf F_{41}^{\times}}
\]
是可逆 Vandermonde 矩阵。因此对每个种子 \(r\)，四十个 (775.4) 的模739线性张成包含全部四十个移像，特别包含 determinant-one 的旧 \(B_r\)。所有旧 \(B_r\) 的实际秩为146，故全部新候选的模739秩至少146。R767 的特征零维数又使它不能超过146。

这证明完整流式候选足够，但并不预先指定哪146个候选会被实际选中或其实际 determinant。程序按种子顺序、每个种子四十个 \(j\) 生成；一旦准确选出146个原 recipe行并计算了非零minor，就结束权二候选生成。不会为了补齐一个无用的表而继续遍历剩余种子。

每次高斯消元都在“已选原行 + 当前候选原行”的转置中取主元列；所保存的基仍是原 (775.4)，从未把模739行组合系数猜升到特征零。

## 5. 原高权和 RR 空间

由 R767 的正常生成，用新的146个 \(K\) 定义形式得到
\[
H^0(r\mathcal L),\quad r=1,\ldots,6,
\]
维数依次为
\[
146,418,690,962,1234,1506.
\]
其候选是新基的普通乘积，明确保存左右子配方索引。原 E4、E6、eta12 均是本算术模型上的定义形式，直接读 R771 的已完成行。在原四个椭圆主部层逐次补两个方向，即得到 \(M_6\) 的694个以及 \(M_{12}\) 的1514个 \(K\) 定义配方。

每层均实际求秩和非零子式；若计算未完成则只保存进度，不注册基已完成。原验证界保留为273、820、1640，所有完整缓存行到1640。层算法的正确性沿用原 R767/R771，并未以另一个商曲线的维数替代。

除以原
\[
D_\star=
\left(\frac{\eta_{\rm Ded}^{12}}2-\frac{\sqrt{-3}E_6}{144}\right)^2
\]
后，得到 \(L(2(t)_0)\) 的1514个 \(K\) 定义函数配方。原 divisor degree1640、cusp常数−1/6912、原 \(q_Y=Q^3\) 都保持。

本次不生成完整特征零长 Fourier 表，也不求实际 \(A,B,y,\beta\) 或高度。它给出下一步所需的全局算术基，随后以 R774 的准确 \(H^3\) 和 R772 的 \(L\) 线性恢复证书继续。需要时仍以 \(M/L\) 四十坐标展开真实行；任何实际达到rank2720的准确部分系统已是完整308维核。

## 6. 运行、断点和输出

新源码：

- scripts/R775_original_K_defined_RR_bases.py；
- scripts/R775_public_K_defined_RR_bases.py；
- notes/R775-public-K-defined-RR-bases-request.json；
- .github/workflows/serre-p41-K-defined-rr-bases.yml。

只在公开仓库 Actions、Python3.12、python-flint0.9.0执行新算术。包装先写原source/request/README收据，读取实际旧run和artifact元数据并核全部manifest/hash，再进入新算术。原发布helper保持原样。

每算完一个新的det移像就保存完整已完成前缀；每四十个trace候选保存选取进度；正常乘积和椭圆主部沿用逐批游标。已完成阶段不重算，失败或80分钟预算只留下未完成凭据和完整断点，随后用同源继续。旧输入保留原tag，新输出有独立tag；续算必须绑定同一核心和原输入hash。

完整系数表、移像表与高权配方仅存artifact；Git只放小证书、小收据、日志和完整SHA清单。最终verify检查实际三组维数、原recipe minor、完整stage hash和诚实的未完成字段，不把方法可行性注册为数值输出。

## 依据

[R771实际结果](../results/R771-certified-original-quotient-RR-bases.md)给全部完成输入与真实minor；[R772](../results/R772-original-RR-descent-and-exact-function-recovery-certificates.md)给原算术模型、半线性下降、真实L未知系数及完整函数验证。R772证明SHA256为30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d。R767的原正常生成和椭圆主部范围通过这两份结果保持不变。
