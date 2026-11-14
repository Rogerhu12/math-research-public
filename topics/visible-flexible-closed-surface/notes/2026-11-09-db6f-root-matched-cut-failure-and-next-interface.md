# matched-cut 原自由联解的闭失败记录与下一接口

状态：数值失败及来源核验；不构成无解结论。作者 /root，2026-11-09。

## 1. 实际闭合的运行

root session5817 于 ed7ae6 启动，ff466f 实际返回 tool exit0；原 Python 也 exit0，因为它捕获并记录了求解异常。其 summary 的 solver_success=false，只有两次真实尾请求，没有最终 prefix CP 和 final seam。外层 guard 耗时1196.728212292秒；原 runner 1195.85056954秒。原121入口和外层133绑定均重核。

首项真 DN/J 成功，原残差1.2533744091676813e−9，705项 Jacobian、17个 jet；这是新 restart 实际 H 的成功，不是旧 warm 的假响应。第二项真实 DN 在原线搜索的 iteration3 失败，norm=2489.354194334243，minA=.05044758616045935，minD=.9915002412989463，chartCondition=39850.69351187304。该失败不否定首项的有限尾成功，也不能推断不存在所求解。

## 2. 正常审计与调用勘误

独立全文审过的 v2 审计器 SHA 00c048161cde786c830199d092b76e4a6027e081eab180e2fc449133515050a7 未再修改。首模式实际320c94/exit0，结果 PASS_FIRST_ACTUAL_DN_J_ONLY；正常最终模式 cc36ed/exit2，结果 ORIGINAL_NUMERICAL_SUCCESS_NOT_ESTABLISHED。最终门没有因 Python exit0 而错误放行。root 真实观察与摘要、响应、来源保存在 root-matched-cut-observed-execution-01。

首模式第一次调用0930fb/exit1因相对输出路径按 repo 而非 topic 解释被拒；没有写输出或调用 solver。之后只改为绝对输出路径，没有改程序或验证门。独立审者发现的路径说明错误单列 prefix-matched-cut-auditor-path-erratum。实际收据合并存于 root-matched-cut-and-call004-audit-executions。

## 3. 原03仍是另一独立运行

原03的call4=505/512同样已闭失败，iteration7/norm=.08018806223955673；原83绑定、八源、实际目标及checkpoint高度、865×30/13×30状态和闭日志已由 aaac43/exit0 核查。保留此前唯一真成功call1=63/64，原控制器减半到call5=1009/1024继续；没有记录控制器退出或把失败状态当warm。其配置仍原36轮、tol2e−9，未改方程和guard。

## 4. 下一研究接口的边界

正在核查的新客户端方案是每次真实 DN 请求从最后真正成功的 H0 沿小步路径走到新的精确 Htarget。中间点只供 warm；只有精确目标按原请求取得真实 Jacobian/audit后才能返回给原自由外层。它与原03逐模幂路径不同，既不由原失败推出它必败，也不预告它成功。尚未实施、尚未启动新求解。须单独冻结策略、所有真实 wire 请求、回退及异常分类，修改实际来源身份，不套用旧八源审计门。

G5、全域新候选证书、N512复求及未参与者完整复跑仍未完成。
