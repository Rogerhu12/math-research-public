# R852：原五个单 Z 系数的准确十四坐标、秩五与常数项表达式

日期：2026-11-16。状态：**已由本公开仓库 Actions 实际完成。**
本结论消费原 R791/R844/R846，接 [ZA](../notes/2026-11-16-original-three-isogeny-sigma-and-one-Z-period-contraction.md)
和 [执行方法](../notes/R852-original-one-Z-coefficients-consumer-method.md)。
实际原 $p=41$、$f=f_4$、$\deg f=1206$、$c_1$ 和 $z=a-1$ 全部保持。

## 1. 实际结论

在原十四次域 $L=\mathbf Q(b,\zeta)$ 中，五个
$$
C_j=3\left[(2-p_j/q_j)a+\rho_j\sigma^j(a)
+\sigma^{-j}(\rho_j^{-1}a)\right],\qquad a=h_f,
$$
已经准确展开为
$$
1,b,\ldots,b^6,\ \zeta,\zeta b,\ldots,\zeta b^6
$$
中的十四个约分有理坐标。五列的准确有理秩为 **5**，故每个 $C_j\ne0$。
实际非零 $5\times5$ 子式选的是原坐标行 $0,1,2,3,4$ 和五个全部系数列；
非零有理行列式及完整坐标保存在下列完成产物中。此处未用辅助素数的秩代替准确秩。

五个
$$
D_j=3c_jh_{g_j},\qquad
c_j=\frac{y(T^jf)-y(f)}{x(T^jf)-x(f)},\qquad g_j=(1+T^j)f,
$$
也已经生成准确的原表达式。它们仍通过原四响应定义点值，
本结论不称 $D_j$ 已展开为有理坐标。

ZA 给出的同一个椭圆一阶行保持为
$$
3(B_{g_j}-p_j B_f/q_j)
=7\,\operatorname{tr}_{\chi,L}(C_jZ+D_j),\qquad
Z=\mathcal Z_b(f(c_1)),\quad
\operatorname{tr}_{\chi,L}=\frac{c_\chi}{14}\operatorname{Tr}_{L_{41}/\mathbf Q_{41}}.
\tag{852R.1}
$$
外因子7、原角色尺度、完整 Galois 作用和 $T^7=\zeta^2$ 都保留。
五个 $C_j$ 的线性独立不等于五个 (852R.1) 值、完整原高度或高度行列式非零。

## 2. 准确来源和证明

由 R791 全部原微分向量上的准确作用，
$$
h(Tu)=\rho\,\sigma(h(u)),
$$
因而
$$
C_j=h\!\left(3[(2-p_j/q_j)I+T^j+T^{-j}]f\right).
\tag{852R.2}
$$
原 R844 已保 $T^jf$ 的十二坐标；负方向只将已经认证的原整数 Hom 矩阵应用于新的右端，
使用 $T^{-j}=T^{21-j}$，没有将七次绕回的相位删掉。
将所得有理线性组合与 R791 的十二条准确切向配对，
即得到上述十四坐标。新有理消元给出实际非零子式，证明秩5。

全部733个原一阶节点逐字继承，包含原529个点节点。新程序共 **839** 节点，
即106个新标量组合节点。原五个 secant、对应非零分母与逆、
五个 $\rho_j^{-1}$、六个原切向根均直接引用既存节点。
因此新点加法数和新 inverse 数均为 **0**。
完整 $\sigma$ 节点依旧作用于原 unit-chart 与全部常数，不只替换 $b$。

三项新数学阶段为原源 audit、839节点程序、五组准确坐标及有理秩子式。
完成证书同时绑定新程序、准确坐标阶段和所有原 source identities。
本地只读取实际产物、核字节 SHA 和来源/tag/字段，不重跑任何数学阶段。

## 3. 实际公开运行与关键产物

- Run [43801628875](https://github.com/Rogerhu12/math-research-public/actions/runs/43801628875)，compute job 133083063775。
- Source commit：d0023643ba47099947b6753010d8e7c8120a214c。
- Core SHA256：2fc8df00b14e14f275a40250ee48bb4a6d076ace1a4ff4017ff421233e9e42cb。
- Wrapper SHA256：873097d8462f1f20d8cb05adb2e5b3261bbea44a1a58de12a05e9286970dee3c。
- Method SHA256：e4a4e9838343fe6b1aebe8e7ec0565c79859abfc8863b27e40bdf2fe94617358。
- 完成时间：2026-11-16 04:02:53.806861 UTC；core 数学时间0.035879553秒。
- Configuration SHA256：f15d53fdcc6f22ae197a3fcc9110c5729bbae2220beca0f6d8844c4121d68e1a。

| 实际文件 | bytes | SHA256 |
|---|---:|---|
| p41-original-one-Z-coefficients-certificate.json | 7615 | e9acbfa243d1fb3e5dca1b053f1e344d680edf5fd6e623ebe05cd74a0232ce40 |
| R852-one-Z-coefficient-program.json.gz | 102873 | bf0a518c81b61a8a0cf2dca9a73cf07397a9fd2c737a40e73b4c0f7d6935e3b6 |
| R852-one-Z-five-exact-C-coordinates.json.gz | 17253 | 621199e5ac259d7a8993e3dfedf540bb37635a997a742cff4436562872d0570e |
| R852-one-Z-stage-manifest.json.gz | 3199 | ea2102869e32944af500d4efd769b1ac7d0e811ec243dd1f1d743b1ced580699 |
| full-outputs-manifest.json | 1918 | dde01718b0bbe90f052a166cb8b8072345b3e9a4e156ec2a9be5bbf72447f301 |

完整 manifest 有11个实际产物，另有 manifest/reference 本身。
Artifact 14196442913，名称 serre-global-R852-original-one-Z-coefficients-43801628875-1，
2743138 bytes，整 ZIP SHA256
01ae4657b56387080bc44b9f10b841e0c29499ffce02e2046b1a3794c26cd45d，
到期时间2026-11-17 04:02:53 UTC。根会话已实际读取并重哈希整个2.74MB ZIP，
再按完整 manifest 读取全部11个产物；这里不是仅复述 API 的 archive digest。

## 4. 直接继承与未完成范围

唯一直接源为原 R847 的九件必要成员，其原输入包保270个准确原叶；
本次不下载 GLOBAL 大包，也不重原 Hensel、Dixon、点加法、Hom 矩阵、
切向或辅助素数非零见证。新的最小输入包
R852-one-Z-retained-original-inputs.tar.gz 为2529608 bytes，SHA256
44d40476878e6de8a2121e81b2ab6f68e57d3b4c19857119095f7477e978f8b4，
保九件原成员的原字节、完整父子身份及270叶载体。
原来源仍是原 producer；重新封装没有改变其 tag。

准确坐标、原程序和必要输入仅保于一日 Actions artifact，不进 Git 或 Release。
仓库保本证明、源码、请求参数和简短身份/SHA。

实际41四响应球、$Z$、展开的 $D_j$、原 $Y$-Picard period、原高度、A.1
准确零与全素数一致性均未由本次计算完成。后继仍须按41C取得真实41球、
原分母赋值和完整尾；原五个椭圆方向以外的 $Y$、$\ell_h$、非41项和刚性化常数不删。
