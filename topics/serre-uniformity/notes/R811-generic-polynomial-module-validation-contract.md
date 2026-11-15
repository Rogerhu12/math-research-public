# R811 多项式模块的公开 generic 验证契约

日期：2026-11-15。这里验证同一个精确多项式模块及真实中断续算机制，
不把 generic 输出冒称原 CM 模型的 A/B 或极除子。

实际数学只在本公开仓库 Actions。固定 python-flint 0.9.0；
复用源码SHA固定的R754 QKField表示，但取明确不同的
$L_{\rm gen}=\mathbf Q(c,\zeta)$，$c^7=2$。
由Eisenstein及7、2互素，字段次数为14。

取 $u^2=z$、正规基 $(1,u)$，$\alpha=c+\zeta$，原分式
$$
 f=\frac{u^2-\alpha^2}{(u-\alpha)^2}.
$$
共同因子 $u-\alpha$ 需要真实消去；完整极理想为 $(u-\alpha)$，
不是直接把原分母理想当极理想。第二图 $t=1/z,\ v=1/u$，
基变换是 $D=\operatorname{diag}(1,t^{-1})$。

两个图分别构造不可变原 $P=[M_p,-M_q]$，完整unimodular列约化、
逆时间左乘原操作恢复整个核、联合Hermite得到 $[H;W]$。
最后对独立原P核全部 $M_pH=M_qW$。
手写闭式H/W在测试中逐项核验；例如第一图的两联合列是
$$
 (1,-\alpha^{-1},-1,-\alpha^{-1})^t,\qquad
 (0,z-\alpha^2,2\alpha z,z+\alpha^2)^t.
$$
第二图分别为
$$
 (1,-\alpha,1,\alpha)^t,\qquad
 (0,t-\alpha^{-2},-2\alpha^{-1}t,-t-\alpha^{-2})^t.
$$
此外准确核两向Laurent包含、第一图长度1与第二图遗漏零纤维长度0，
并独立用普通系数卷积核packed stride13的最高c次数12乘法。

先不中断运行，再在四个确定原子边界真实调用os._exit(97)：
完成tile后、写完操作receipt后、原子current提交后、cleanup已删一个旧tile后。
每个模式重新启动原进程，完整最终数学结果文件必须与不中断基线逐字节SHA相同。
故这会检出失去旧列、漏恢复操作、乘逆而非原操作及不安全裁剪等实际风险。
它不是仅构造相同对象再比较，也没有把fault标签或路径放进数学身份。

原R811乘法、原R815导子与其真实来源可以独立激活；
本generic测试不是附加审批门。真实原模型完整极理想仍必须读取真正完成的
原A/B乘法、保原b字段及两图，再核全部272维恒等式。
本稿没有预填测试成功或原极除子。

源码与request逐SHA绑定；workflow仅contents:read，断点/收据保留一日。
可重算raw、证书不入Git/Release，只登记source/run、实际结论与必要SHA。
