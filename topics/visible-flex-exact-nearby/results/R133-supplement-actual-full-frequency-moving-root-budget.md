# 当前完整moving根：实际全频逆与参数圆盘预算

**已证：** 在[完整moving根标量化](R133-supplement-complete-moving-root-scalarization.md)
的同一个完整角空间中，实际Neumann常数严格小于0.131785809731，因而小于3/20。
这里保留独立even mean方程；只有求A逆时使用mean-zero空间，并非删除原Jacobi的mean。

公开 [run43594466882](https://github.com/Rogerhu12/math-research-public/actions/runs/43594466882)
实际13门全部通过，数学child和wrapper都返回0。event commit为
`b84d9851a03b01ce4bac12cd810a906ea9424fd5`，实际科学checkout为
`f61ca9786a5a5b60bb9d6066686aad97cfb9faac`。两者不同，原过程已分别记录。
producer计时0.082951341秒，实际child外层0.414779361秒。
主代理已亲读13门、原native、process和全部下列有向界。

| 原件 | SHA256 |
|---|---|
| `complete-moving-root-scalarization.json.gz` | `10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f` |
| child `process.json` | `9f1d18061f1b406f028916adc33484b4deea826a8e4175fd28b0fdb5b690342d` |
| mathematical source | `4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e` |
| 13文件manifest | `b1e47bdc43fdb5f9742ee8feb087f5a66dd72457439405abecb1816012b1c746` |

完整原件位于
`notes/current_root_scalarization_ci/run-43594466882-1/consumers/`；原输出没有重新计算或改写。

## 实际作用域

参数是单一原内禀eta0，以及同一显式族Q_delta=Qbar+delta Z、nu_delta=nu0+delta的
整个复圆盘|delta|≤10^−8。已证R31选择的实delta*严格在其中。这不宣称该族是PDE解。

外径向复域包含每个实际root周围半径10^−5的圆盘，角Wiener宽1/1024。
它全在原piece2549内；完整193个原响应cubic系数来自原part005，准确连续中心offset和
全部193方向repair费逐项加入。其它response分片没有在此执行中重建。
nu紧支集上端9/50严格低于整个根germ，故根处K、b、gamma及根位置准确不随nu_delta改变。

所有表中数均由原有向值向外放宽。same-space界适用于完整Wiener、加权H0及普通L2。
强Sobolev窗口使用正文(N.1)的固定pivot尺度，不用same-space常数代替。

| 完整量 | 严格界 |
|---|---:|
| Neumann因子c | <0.131785809731 |
| J=A^−1，同阶 | <0.229690263530 |
| partial_phi J，同阶 | <0.918761054118 |
| J:H0→H1 | <0.947037217708 |
| J:H1→H2 | <2.455715394335 |
| J:H2→H3 | <14.655021649895 |
| J:H3→H4 | <153.825360913869 |
| J:H^(−5/3)→H^(−2/3) | <1.787479366938 |
| J:H^(−3/2)→H^(−1/2) | <1.525009467031 |
| J:H^(−2/3)→H^(1/3) | <0.947037217708 |
| 全均值绝对值下界 | >1.119707703702 |
| gamma实部下界 | >1.119607700127 |

径向Cauchy和drift commutator仅在半径5×10^−6的内圆盘使用：
||J_r||<45938.052706，完整||[D0,J]||<45938.110973。
这项包含真实投影drift与A_r，没有在根处把二者置零。

完整独立mean行的三个同阶系数上界分别为0.295894114、0.297058285、0.001253754；
ordinary g2的mean泛函范数为1。原source在标量方程的flux内，弱式不要求对g2作径向微分。

## 尚未授予的后继

此预算证明完整angular逆和准确scalarization的定量实例；它没有求出实际两行root连接、
positive high-input graph、root首系数有限常数或完整返回强余项。原band64负窗数值
也不能直接搬到含96模方向的新显式族；新角乘积可到192，必须单独付宽带扰动。
最终真PDE背景的转移、全regular逆与非线性存在性仍继续。

