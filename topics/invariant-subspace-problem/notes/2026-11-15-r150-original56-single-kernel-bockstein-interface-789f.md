# R150：原 56 行单核 Bockstein 的完整外因子接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。  
日期：2026-11-15 UTC。

本接口只使用已完成的原 56×22 模型、三个真实最大子式上界，以及实际完成的模 $f$ 的 21 个单位主元。此前精度二整矩阵重放因 $\mathrm{MemoryError}$ 停止；本入口从保存的第一精度证据构造两个单右端解，全部原 56 行决定真实第二指数。本文未报告新执行结果。

## 1. 精确输入与已付范围

主源码：

~~~text
notes/2026-11-15-r150-original56-single-kernel-bockstein-789f.py
blob 7bcc6dec08648d2c0628ab711c80f81db27f2a92
bytes 30109
SHA256 49a8a83e627d2db1ab76a2b37be6652e956cdd73a55181cc2e95f458a4848674
~~~

完整输入清单：

~~~text
notes/2026-11-15-r150-original56-single-kernel-bockstein-inputs-789f.json
blob 6a6cada19619fc4a05aba9eb84cbd3be0c5da081
bytes 5477
SHA256 313acc450f98c41d0a482fb1eac15ea084a035a63765eab6f953df2c067080d8
~~~

原模型 $A$ 有 56 行、22 列；源级降维与行的非零有理常数缩放由原 core 生成器完整绑定。因此本模型全部最大子式的外部 gcd，正是此前定义的 $\Omega$。六个已局部化因子仍严格为原清单，未新增局部化因子。

三个已完成的真实最大子式给 $\Omega\mid U$。本轮旧源码已经严格分解
$$
U=f^2,\qquad \deg f=60,\qquad \gcd(f,f')=1.
$$
不假设 $f$ 不可约。

旧第二次 300 秒回执：

~~~text
notes/r150-source-kernel-session-789f/43756208221-complete-original56-local-outside-gcd-300-second.json
execution source 8e4025c0ef0ee422077b1fc66ece96d97c3c40e9
actual raw 6043 bytes
SHA256 26917bb0ac3058ce08c57b18f91bca119b42ad866c4264e98ad9d4a02a7382cc
~~~

它保存了全部 21 个模 $f$ 单位主元，完整残块为 35×1 的零块。随后对 $f^2$ 的重放只完成五步，于 generation 27 保存了 51×17 块；原 raw 的错误类型确为 $\mathrm{MemoryError}$。

新程序只流式读取、散列该 177991821 字节压缩文件及其全部解压字节，JSON 解码限于前 21 个第一精度操作对象。精度二矩阵不被解码。每个操作的原行、原列、缩小后位置、pivot、inverse 与相邻矩阵 SHA 链全部核对。由此恢复原 21 行集 $R$、21 列集 $C$ 和唯一剩余原列 $j$。

## 2. 两个单右端与完整 56 行

令 $B=A[R,C]$。按已付主元的次序重建 $B\bmod f$，只消这个 21×21 方块，不再选主元。每个实际 pivot 必须等于已保存的同一 pivot，已保存 inverse 必须在整个 $\mathbb Q[s]/(f)$ 中为真逆。共有
$$
20^2+19^2+\cdots+1^2=2870
$$
个原方块 Schur 坐标。

保存三角因子后，第一次单右端解为
$$
B x_C=-A[R,j]\pmod f,\qquad x_j=1.
$$
每个 $x_i$ 取次数小于 60 的有理多项式代表。程序先核全部 21 个原单位行，再对全部 56 行做严格多项式除法：
$$
Ax=fE.
\tag{2.1}
$$
余式必须逐行严格为零。只在选定 21 行为零不算成功。

第二次单右端使用同一已完成三角因子：
$$
B y_C=E_R\pmod f,\qquad y_j=0.
$$
再次核全部 21 个原单位行。最后用原 56 行计算
$$
w=(E-Ay)\bmod f.
\tag{2.2}
$$
保留 $E$、原乘积 $Ay$、全部 56 个余式、自由坐标以及相应精确商。所有原行运算都作用于同一个已付行常数缩放模型，未把缩放行与未缩放右端混配。

## 3. 完整 gcd 公式

置
$$
g=\gcd(f,w_1,\ldots,w_{56})
$$
并首一化。则
$$
\boxed{\Omega=f\,g.}
\tag{3.1}
$$

证明如下。对 $f$ 的任一不可约因子 $h$，已付同一 $B\bmod f$ 为单位，故模 $h$ 原矩阵的秩恰 21。22 列中只有一个正 Smith 指数，且自由坐标 $j=1$ 的规范核生成该一维核。上界 $U=f^2$ 迫这个正指数不超过 2。

式 (2.1) 给其第一残量；在 $h$ 局部环中 $f/h$ 为单位，因此以 $f$ 除法或以 $h$ 除法定义的 Bockstein 同零。第二个单右端扣除了唯一原单位列像，故该方向能够再升一阶，当且仅当全部 $w_i$ 在模 $h$ 为零。于是指数为 2 当且仅当 $h\mid g$，否则指数为 1。平方自由性保证式 (3.1) 同时准确覆盖全部不可约因子。

程序另外核 $\Omega\mid U$、$g\mid f$ 及
$$
\gcd\!\left(f/g,\ w_1/g,\ldots,w_{56}/g\right)=1.
$$
由
$$
A(x-fy)=f(E-Ay)
$$
还保留自由坐标仍为 1 的完整多项式二位来源。不能因某个余式非零而把整个 $f$ 分支删去；所有分支由这个完整 gcd 同时保留。

若 $g=f$，才得到 $\Omega=f^2$、次数 120。若 $g$ 是真因子，报告实际次数 $60+\deg g$。本接口未预填任一分支。

## 4. 核验与续接

源码内有两个极小 3×2 独立检验，$f=(s-1)(s+1)$，分别给混合指数 $1,2$ 和全部指数 2。二者都具有非零 $E_R$ 和非零纠偏；所得公式与全部三个真实 2×2 子式的 gcd 比较。该检验不替代原 56 行实算。

保存边界如下：

1. 完整原 profile 的小抽取；
2. 每个完整 21×21 主元；
3. 完整第一单右端；
4. 每批四个完整原 $Ax=fE$ 行；
5. 完整第二单右端；
6. 每批四个完整原 $E-Ay$ 行；
7. 完整 gcd 及来源证书。

每个边界采用两槽文件及原子 pointer。未完成的一个主元或行批不改变上一个提交状态。已完成的三角因子另作同绑定的临时文件，后续两 RHS 不重新因子分解。

程序将错误类型和信息放在 $\mathrm{parameters.error}$，使会话小摘要仍可准确保留失败原因。预算、绝对路径不进入语义绑定，源字节与全部原输入 pins 进入绑定。续跑使用同源码、同 out；完整证书已存在时直接消费，不重新解单位块。

## 5. 实际 CLI 与预算

~~~sh
python3 {scripts}/2026-11-15-r150-original56-single-kernel-bockstein-789f.py \
  --lower-source {scripts}/2026-11-15-r150-complete-original56-local-outside-gcd-789f.py \
  --upper-source {scripts}/2026-11-15-r150-original-three-minor-determinant-upper-789f.py \
  --core-source {scripts}/2026-11-15-r150-original-global-projection-polynomial-core-789f.py \
  --parent-checkpoints {work}/original-global-projection-polynomial/checkpoints \
  --upper-out {work}/original-three-minor-determinant-upper \
  --profile-out {work}/complete-original56-local-outside-gcd \
  --out {work}/original56-single-kernel-bockstein \
  --remaining-seconds 300 \
  --memory-mib 2048
~~~

共享数学预算 300 秒，地址空间 2048 MiB，外层墙钟 360 秒。首次实际解析与数学运行由上述 Actions 步骤完成；本文不声称本地 AST、编译或数学测试已经执行。

小回执：

~~~text
{work}/original56-single-kernel-bockstein/original56-single-kernel-bockstein-receipt.json
~~~

临时状态：

~~~text
{work}/original56-single-kernel-bockstein/checkpoints/
~~~

真正完成必须同时保以下门：

- 21 个 paid pivot 与 inverse 全部重现；
- 2870 个原方块坐标身份；
- 两次共 42 个原单位行产品；
- 全部 56 行 $Ax=fE$；
- 全部 56 行 $E-Ay$ 的原乘积与余式；
- 完整平方自由支撑 gcd 和真实上界整除。

代码、参数、小回执和 SHA 可长期登记；所有可重算矩阵、核、商、三角因子和来源只存当前作业临时目录。

## 6. 数学结论的边界

这是原投影外部最大子式 gcd 的完整证书接口。它不声称原 4367×6188 模型的高正常部分已经消掉，也不把原投影的 $\Omega$ 当作全部原目标的湮没多项式。最新 $J$ 的实际维数为 1；即使本步骤得次数 120，仍只能将当前全原剩余乘子次数界收至 21，不能据此宣布九个 $h_*$ 平方或精确 $31^2h_0$ 来源已经闭合。
