# R844：原五个 Hom 加法点与原比较函数值的准确 DAG

日期：2026-11-16。状态：**本项实际完成；原全局极除子、刚性化与高度仍未完成。**

公开任务 run **43780702248**、job **133017074300**，source
**5ebcfafb1c0bf72618a50de1f974c5d46d13ff58**，实际数学用时
**0.022079986999997914 秒**，3个数学阶段。最终程序有529个节点，
其中 R841 的原50节点逐字导入；五个新加法均实际走不同且非相反的原 Hom 字分支。

本项读取 R843 已证出的同一原点非挠性，不使用 R840 的短有理重构候选。
输出是原数域中有完整来源和非零证明的准确算术表达式，不声称已展开成十四个有理坐标。

## 1. 实际完成的五个原输入

始终取 R791 的原第4号整数 Hom
\(f=f_4:X_L\to C_b\)，\(\deg f=1206\)，
\(\mathcal T=D_{\rho^{-1}}\sigma\)，\(\mathcal T^7=[\zeta^2]\)，
以及 \(\alpha_3=1-\zeta^2\)。本次严格采用

\[
g_j=(1+\mathcal T^j)f,\qquad
g_{R,j}=[\alpha_3]g_j=f_R+\mathcal T^jf_R,\qquad 1\le j\le5.
\tag{844.1}
\]

这五项是原 R791 的五个 \(\eta\) 方向；不是 R794 所选的另一组五个低次映射。
真实输出的原次数、比例与实下降字，均逐项绑定原 R791 已成文件。

| \(j\) | 原 \(r_j=a_j/b_j\) | \(\deg g_j\) | \(\deg g_{R,j}\) | 实际加法分支 |
|---:|---:|---:|---:|---|
| 1 | \(31/67\) | 2970 | 8910 | 不同且非相反 Hom 字 |
| 2 | \(-41/67\) | 1674 | 5022 | 不同且非相反 Hom 字 |
| 3 | \(-34/67\) | 1800 | 5400 | 不同且非相反 Hom 字 |
| 4 | \(34/67\) | 3024 | 9072 | 不同且非相反 Hom 字 |
| 5 | \(103/134\) | 3339 | 10017 | 不同且非相反 Hom 字 |

每个 \(g_j(c_1)\) 和 \(g_{R,j}(c_1)\) 均给出原 \(L\) 中的准确 \(x,y\) 根节点。
还给出每项的七个真实 \(\sigma\) 共轭分量，连同各自的共轭目标曲线常数。
不为这七分量重新做35次独立点加法。

## 2. 准确分母与点加法为何成立

R841 已给原
\[
P=f(c_1)=
\left(\frac{3h_0(A_0^2-bB_0^2)}{A_1B_0-A_0B_1},
      \frac{A_0}{B_0}\right),
\tag{844.2}
\]
其中四个响应、\(h_0\)、原目标 \(b\) 都是来源完整的准确单位解表达式。

R843 进一步从同一原点的真实518位响应证明 \(P\) 非挠，并用
原 \(\beta\in A(\mathbf Q)\) 与原因子的 \(\mathbf Q\)-单性，
证明每个非零原 \(L\)-Hom 在 \(\beta\) 上的值非挠。
于是同一原目标上的整数 Hom 字准确决定 \(O\)、相等与相反：

- 零 Hom 字给 \(O\)；非零字的值非挠。
- 两字不同且不相反时，两点的 \(x\) 不等。
- 非零字的点既不是二挠也不是三挠，故 \(y\ne0\)、\(x\ne0\)，
  从 \(y^2-b=x^3\) 得 \(y^2-b\ne0\)。

本次读取原 \(\mathcal T\) 整数矩阵，形成五个 \(1+\mathcal T^j\) 字，
逐项确认是非零字，且五次输入均不同、不相反。
原普通加法公式的
\[
m_j=\frac{y_{\mathcal T^jP}-y_P}
          {x_{\mathcal T^jP}-x_P},\quad
x_{g_j}=m_j^2-x_P-x_{\mathcal T^jP},\quad
y_{g_j}=m_j(x_P-x_{g_j})-y_P
\tag{844.3}
\]
因此有准确非零分母证书。这不是用有限精度的非零或零来判加法分支。

指定三同源仍逐项保留原公式
\[
x_{g_{R,j}}=-\frac{\zeta}{3}\,
 x_{g_j}\frac{y_{g_j}^2+3b}{y_{g_j}^2-b},
\qquad
y_{g_{R,j}}=
 \frac{y_{g_j}(y_{g_j}^2-9b)}
      {3\varsigma(y_{g_j}^2-b)},\qquad \varsigma=1+2\zeta.
\tag{844.4}
\]
实际新 Hom 字经 \(1-\zeta^2\) 作用后，与 R791 已存的
原五个实下降字逐项相等。没有替换原 \(\kappa\)、\(v\)、目标相位或三同源常数。

## 3. 完整 Galois 运输及原比较函数值

\(\sigma\) 作用于整个准确表达式，包括全部单位解叶、矩阵条目、右端和常数。
消费者不只变换外层系数，也不把某一个辅助分支的数值当作准确叶。
回到同靶的 \(\mathcal T^j\) 使用原 \(\rho_j^{-1}\)，
\(x,y\) 分别乘其平方、立方；\(\mathcal T^7=[\zeta^2]\) 的相位保留。

令 \(Y_u=y_{u(c_1)}\)。本次还给出五个准确非零值
\[
\mathcal R_j(c_1)=
 \frac{N_{L/K}(Y_{g_j}^2-b)^{\,b_j}}
      {N_{L/K}(Y_f^2-b)^{\,2b_j+a_j}}.
\tag{844.5}
\]
每个范数按七个真实 \(\sigma\) 共轭相乘，目标常数同时变为 \(\sigma^k b\)。
原点非挠已保证各因子非零。上述值直接使用原 R791 的次数比例与比较函数定义。

若后继另改写为同靶 \(\mathcal T\) 点的乘积，必须保留
\(N_{L/K}(b)/b^7\) 的常数，总指数为 \(-b_j-a_j\)。
本次实际采用真实 \(\sigma\)-范数，未作这种省略常数的改写。

原 \(\kappa v^\dagger v\) 的五方向规范从 R791 逐字读取。
输出明确记录：尚未应用原 \(c_0\) 刚性化，尚未计算五个全局极除子，
也未计算 Picard 比较、原 \(\eta\) 或任何高度。

## 4. 实际来源、产物与字节身份

本项仅消费已经完成的四组来源：
CM 原165件、R791 原9件、R841 DAG 原11件，以及 R843 原66件，
合计 **251件**。R843 是原点本身的非挠证书；
不是短候选或另一点的非挠证书。父子配置身份全部原样绑定。

| 项目 | 字节 | SHA-256 |
|---|---:|---|
| 核心 R792_original_Hom_word_point_DAG.py | 26566 | 719c170ac00cf7b15db0d74b5a58998f2901ad838db33dc9d01fd29acd36805a |
| 封装 R792_public_original_Hom_word_point_DAG.py | 24901 | bb0cce85ff6e4f7df2dd9e4a153b21e6e1a14038ee35800ec9c91f7edecfda9a |
| 实际请求 R792-Hom-word-point-DAG-public-request.json | 5122 | 3d36761a303ce52930869302b33a2865894232606b053ca269f86ce84ccb7674 |
| 工作流 serre-R792-Hom-word-point-DAG.yml | 6986 | 0e33bba7a0493b2e1b72197fe36b66007392dda7d92a1787417b0a74891d19a6 |
| 最终 certificate | 6822 | 57a2e3ec0b18c6a49e7c4cbfba23a4bda347384788f6b075e6dd8d0b7cf0ee41 |
| 五加法 point-program | 68403 | 97a8fb3f185660468e6637358c9c29b34bfe8630599f36fa7e7f58ef6acb582b |
| 原 \(\eta\) 规范阶段 | 3123 | 11e67f7134bd5838a5d8499907f78a3f78c59da4681320569ac2b66bc7006eb3 |
| 原来源审计阶段 | 3161 | 7b2e6752245264f533c8aa55f71d352d75a9478319975980ac819b99c764c507 |
| 数学阶段 manifest | 2942 | 9d52a4a26b63b72454362f9c8523615addc130b890769de140f76f27769ec85c |
| 全输出 manifest，11件 | 1653 | b21b40d4636a4c6a663ca0648c8a179e8ba89f22c966d37ba695779881130ef4 |
| manifest reference | 184 | 4d830219d1900a870611049a543b04cc4bc8a00785041b4bd365e1823e644a90 |
| 251件必要输入 carrier | 1816125 | 479f587a0b67611f41f07cb616725620ee430df9d7e7f0305bf49ab40fa66bcb |
| 输入 receipt | 56043 | 0213e1cadb7f880294d6eb0197d553dc474e67b3954bf367dceff905fdf2958f |
| public-actions-input | 58774 | 282d4c2bf44995cd9ae8306f70cf35c9cbe1984a97ece39fe3c7b2965e06fcdd |

最终文件名为 p41-original-Hom-word-point-DAG-certificate.json；
程序为 R792-Hom-word-DAG-five-addition-point-program.json.gz；
数学 manifest 为 R792-Hom-word-DAG-stage-manifest-04b3cac8b0738d6fa5a65aa4.json.gz。
配置 SHA-256：
**fbbcb4721a30e7d39a165db6d9453826199493feb78ae6e2920a06c8473e9da5**。

原 run 回执于 **2026-11-16T00:30:22.557846+00:00** 结束，exit0、error=null。
core 回执362B、SHA f0a5cebbee127fefa7f23104390521f97e2899baca8e310d58620c462cb60a9a；
run 回执400B、SHA 2c1256ae092bc841420653607517ae9e8805b3e90c832702344d4f7a7aa53343。
核心含初始化总时间0.027711522000004152秒，与上述实际数学阶段计时口径分开。

一日 artifact **14188376841**，
名称 serre-global-R792-Hom-word-point-DAG-43780702248-1，
**2020829B**，SHA-256
**dd4c04a120c9253ad5cd39009e62038041e08c44ea6018d417082fe8cbfb11b2**，
到期 **2026-11-17 00:30:22 UTC**。
本地只作完整ZIP及13个成员的 IO/SHA/schema 阅读，没有运行新数学。
Git只留本简明登记、脚本、参数与证明；原程序节点、机器证书及 carrier 不入Git或Release。

## 5. 已完成边界及继续消费

本项把 R843 的非挠结论实际接到原五个 \(\eta\) 映射所需的点加法，
以及原比较函数在 \(c_1\) 的准确值。旧 CM、Dixon、原 Hom 矩阵、非挠乘法和原50节点均未重算。

准确展开坐标、原(A.1)的单值零证、抽象 \(A\) 坐标前像、
全局五极除子、\(c_0\) 刚性化、\(\eta\) 与高度均未由此得到。
全局极理想继续从原全局函数和两图完整理想推进；
原(A.1)则继续使用其准确转置接受接口。
本项3个完成阶段不再重跑，后继只读取上述程序及必要原载体。

## 来源

- [R791：原整数Hom、实下降与五个原η方向](R791-certified-original-Hom-descent-and-eta-inputs.md)。
- [R841：原CM点与指定下降点准确表达式](R841-certified-original-CM-point-and-descent-DAG.md)。
- [R843：同一原点非挠与Hom值分离](R843-certified-original-CM-point-nontorsion-and-Hom-value-separation.md)。
- [本项准确接口与非零分母证明](../notes/R792-original-Hom-word-point-DAG-after-nontorsion.md)，
  SHA-256 39880a1f21f33e49aad0117de3e15568b54f6c78ed3e0c6ccc1b1be235c2836e。
